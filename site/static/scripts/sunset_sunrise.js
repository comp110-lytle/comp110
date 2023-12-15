// USAGE: to get Sunrise, pass false; to get Sunset, pass true

function getSunriseSunset(wantsSunset, latitude, longitude) {
    var datetime = new Date(); // Works Cited: http://edwilliams.org/sunrise_sunset_algorithm.htm

    var year = datetime.getFullYear(); // would be 2021, for instance
    var month = datetime.getMonth() + 1; // 0-11, so Sept. would be 8; hence + 1
    var day = datetime.getDate(); // 1-31, as you'd expect
    var dow = datetime.getDay();

    var zenith = 90; // Apparently what angle counts as sunrise is up for debate?? IDK, 90 seemed like a consensus. Might need some adjustment


    var N1 = Math.floor(275 * month / 9);
	var N2 = Math.floor((month + 9) / 12);
	var N3 = (1 + Math.floor((year - 4 * Math.floor(year / 4) + 2) / 3));
	var N = N1 - (N2 * N3) + day - 30;

    var lngHour = longitude / 15;

    if(wantsSunset) {
        var t = N + ((18 - lngHour) / 24);
    } else {
        var t = N + ((6 - lngHour) / 24); 
    }
    
    var M = (0.9856 * t) - 3.289; // Sun's mean anomaly
    var L = M + (1.916 * Math.sin(toRadians(M))) + (0.020 * Math.sin(toRadians(2 * M))) + 282.634 // Sun's true longitude

    if(L > 360) {L = L - 360}
    if (L < 0) {L = L + 360}

    var RA = toDegrees(Math.atan(0.91764 * Math.tan(toRadians(L)))); // Sun's right ascension

    if(RA > 360) {RA = RA - 360}
    if (RA < 0) {RA = RA + 360}

    var Lquadrant  = (Math.floor(L / 90)) * 90;
	var RAquadrant = (Math.floor(RA / 90)) * 90;
	RA = (RA + (Lquadrant - RAquadrant)) / 15; // Making sure L and RA are in the same quadrant, then convert to hours

    var sinDec = 0.39782 * Math.sin(toRadians(L));
	var cosDec = Math.cos(toRadians(toDegrees(Math.asin(sinDec)))); // calculating Sun's declination; Also technically the toRadians and toDegrees cancel, but just to be sure my logic works

    var cosH = (Math.cos(toRadians(zenith)) - (sinDec * Math.sin(toRadians(latitude)))) / (cosDec * Math.cos(toRadians(latitude))); // Sun's local hour angle

    if(wantsSunset) {
        var H = toDegrees(Math.acos(cosH)) / 15;
    } else {
        var H = (360 - toDegrees(Math.acos(cosH))) / 15;
    }

    var T = H + RA - (0.06571 * t) - 6.622 - lngHour;

    T = T - 5; // Convert to EST

    if(IsDST(month, day, dow)) {
        T = T + 1 // Adding an hour for Daylight Savings
    }

    if(T > 24) {T = T - 24}
    if (T < 0) {T = T + 24}

    return T;
}

function toRadians (angle) {
    return angle * (Math.PI / 180);
}

function toDegrees (angle) {
    return angle * (180 / Math.PI);
}

function IsDST(month, day, dow) { // Works cited: https://stackoverflow.com/questions/5590429/calculating-daylight-saving-time-from-only-date
        //January, february, and december are out.
        if (month < 3 || month > 11) { return false; }
        //April to October are in
        if (month > 3 && month < 11) { return true; }
        previousSunday = day - dow;
        //In march, we are DST if our previous sunday was on or after the 8th.
        if (month == 3) { return previousSunday >= 8; }
        //In november we must be before the first sunday to be dst.
        //That means the previous sunday must be before the 1st.
        return previousSunday <= 0;
}

function getSunrise(latitude, longitude) {
    return getSunriseSunset(false, latitude, longitude);
}

function getSunset(latitude, longitude) {
    return getSunriseSunset(true, latitude, longitude);
}