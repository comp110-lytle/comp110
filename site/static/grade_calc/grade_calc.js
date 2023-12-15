const NUM_QUIZZES = 3
const NUM_EX = 10
const NUM_RD = 3
const WEIGHTS = {
    "EX" : .35,
    "LS" : .1,
    "CQ" : .1,
    "QZFN" : .4,
    "RD" : .05
}

function set_rel() {
    document.getElementById("relative").setAttribute("class", "grade-type-selected");
    document.getElementById("absolute").setAttribute("class", "grade-type-unselected");
    document.getElementById("qz01cb").checked = false;
    document.getElementById("qz02cb").checked = false;
    document.getElementById("qz03cb").checked = false;

    let elements = document.getElementsByTagName("input")
    Array.from(elements).forEach(element => {
        element.setAttribute("value", undefined)
    });

    document.getElementById("final-grade").value = 0
}


function set_abs() {
    document.getElementById("absolute").setAttribute("class", "grade-type-selected");
    document.getElementById("relative").setAttribute("class", "grade-type-unselected");
    
    let elements = document.getElementsByTagName("input")
    Array.from(elements).forEach(element => {
        element.setAttribute("value", 100)
    });
}

function ls_toggle() {
    let div = document.getElementById("ls-sec");
    if (document.getElementById("ls-toggle").checked === true) {
        div.style.display = "inline-flex";
    } else {
        div.style.display = "none";
    }
}


function calculate_grade() {
    if (document.getElementById("relative").getAttribute("class") === "grade-type-selected") {
        calculate_rel();
    } else {
        calculate_abs();
    }
}

function calculate_abs() {
    let avg = 0;
    avg += Number(document.getElementById("ex-avg").value)*WEIGHTS["EX"];
    avg += Number(document.getElementById("rd-avg").value)*WEIGHTS["RD"];
    avg += Number(document.getElementById("ls-avg").value)*WEIGHTS["LS"];
    avg += Number(document.getElementById("cq-avg").value)*WEIGHTS["CQ"];
    avg += Number(qz_avg());
    
    document.getElementById("final-grade").value = avg.toFixed(2);
}

function calculate_rel() {
    let avg = 0;
    let correction = 1;
    console.log(correction);

    if (Number(document.getElementById("ex-avg").value)*WEIGHTS["EX"] !== 0) {
        avg += Number(document.getElementById("ex-avg").value)*WEIGHTS["EX"];
    } else {
        correction -= WEIGHTS["EX"];
    }
    
    if (Number(document.getElementById("rd-avg").value)*WEIGHTS["RD"] !== 0) {
        avg += Number(document.getElementById("rd-avg").value)*WEIGHTS["RD"];
    } else {
        correction -= WEIGHTS["RD"];
        console.log(correction)
    }

    if (Number(document.getElementById("ls-avg").value)*WEIGHTS["LS"] !== 0) {
        avg += Number(document.getElementById("ls-avg").value)*WEIGHTS["LS"];
    } else {
        correction -= WEIGHTS["LS"];
        console.log(correction)
    }

    if (Number(document.getElementById("cq-avg").value)*WEIGHTS["CQ"] !== 0) {
        avg += Number(document.getElementById("cq-avg").value)*WEIGHTS["CQ"];
    } else {
        correction -= WEIGHTS["CQ"];
        console.log(correction)
    }

    if (Number(qz_avg()) !== 0) {
        avg += Number(qz_avg());
    } else {
        correction -= WEIGHTS["QZFN"];
        console.log(correction)
    }

    console.log(correction)
    avg = avg/Number(correction)
    console.log(avg);
    
    document.getElementById("final-grade").value = avg.toFixed(2);
    
}


function avg_1drop(id_format, quantity) {
    let sum = 0;
    let min = Number(document.getElementById(id_format + 0).value);;
    let curr = 0;
    let und_count = 0;
    let relative = false;
    if (document.getElementById("relative").getAttribute("class") === "grade-type-selected") {
        relative = true;
    }

    for (let i = 0; i < quantity; i++) {
        if (i >= 10) {
            id_format = id_format.replace('0', '');
        }

        
        curr = Number(document.getElementById(id_format + i).value);

        sum += curr;
        if (curr === 0) {
            und_count += 1;
        }

        min = Math.min(curr, min)
    }

    if (relative) {
        quantity -= und_count;
        if (und_count === 0) {
            sum -= min;
            quantity -= 1;
        }
    } else {
        sum -= min;
        quantity -= 1;
    }

    document.getElementById(id_format[0] + id_format[1] + "-avg").value = (sum/(quantity)).toFixed(2);

    return sum/(quantity - 1);
}


function avg_2drops(id_format, quantity) {
    let relative = false;
    if (document.getElementById("relative").getAttribute("class") === "grade-type-selected") {
        relative = true;
    }
    console.log(sum, " sum");
    
    
    let min = [Number(document.getElementById(id_format + '0').value), Number(document.getElementById(id_format + '1').value)]
    let sum = 0;
    let curr = 0;
    let und_count = 0;
    
    for (let i = 0; i < quantity; i++) {
        if (i >= 10) {
            id_format = id_format.replace('0', '');
        }


        curr = Number(document.getElementById(id_format + i).value);
        if (curr === 0) {
            und_count += 1;
        }

        sum += curr;

        if (min[0] > curr) {
            if ((relative && curr !== 0) || !relative) {
                min[0] = curr;
            }
        } else if (min[1] > curr) {
            min[1] = curr;
        }
    }
    
    if (relative) {
        quantity -= und_count;
        if (und_count === 1) {
            sum -= min[0];
            quantity -= 1
        } else if (und_count === 0) {
            sum -= min[0];
            sum -= min[1];
            quantity -= 2;
        }
    } else {
        sum -= min[0];
        sum -= min[1];
        quantity -= 2;
    }
    

    document.getElementById(id_format[0] + id_format[1] + "-avg").value  = (sum/(quantity)).toFixed(2);
    return sum/(quantity);
}


function qz_avg() {
    let avg = 0;
    let qz01 = 0;
    let qz02 = 0;
    let qz03 = 0;
    let final = 0;
    let quantity = 0;
    let quiz_weight = WEIGHTS["QZFN"]/(NUM_QUIZZES + 1);

    let relative = false;
    if (document.getElementById("relative").getAttribute("class") === "grade-type-selected") {
        relative = true;
    }
    
    if (document.getElementById("qz01cb").checked === true) {
        qz01 += Number(document.getElementById("qz01").value);
        quantity += 1;
    }

    if (document.getElementById("qz02cb").checked === true) {
        qz02 += Number(document.getElementById("qz02").value);
        quantity += 1;
    }

    if (document.getElementById("qz03cb").checked === true) {
        qz03 += Number(document.getElementById("qz03").value);
        quantity += 1;
    }

    final += Number(document.getElementById("final").value);

    if (quantity >= NUM_QUIZZES) {
        let min_qz = Math.min(qz01, qz02, qz03);
        if (min_qz < final) {
            avg -= min_qz * quiz_weight;
            quantity -= 1
        }
    }

    if ((relative && final !== 0) || !relative) {
        console.log(final)
        avg += final * (WEIGHTS["QZFN"] - quiz_weight*quantity);
    }
    

    avg += quiz_weight * (qz01 + qz02 + qz03)


    return avg
}