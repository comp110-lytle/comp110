/**
 * Handlers "dictionary" associates string handlers with callback functions.
 * The convention of this site is to give the body tag of a page an id along
 * the lines of "{name}-page" such as "{home}-page". Then, to run specific code
 * on that particular page, add an entry in handlers where the key is {name} and
 * the value is the callback function. See below `main` for example handlers.
 */
const handlers = {};

/**
 * Dynamically dispatch based on body's id.
 */
const main = () => {
    const body_id = document.body.id;
    if (body_id.endsWith("-page")) {
        const handler = body_id.replace("-page", "");
        if (handlers[handler]) {
            handlers[handler]();
        }
    }
};

/** Handlers */

handlers["home"] = () => {
    // console.log("Home page handler!");
    // console.log(moment());

    // const home_cal = document.getElementById("home-calendar");
    // home_cal.parentNode.classList.add("col-12");
    // home_cal.parentNode.classList.remove("col-sm-8");
};

/* Call main once document is loaded. */
window.addEventListener("load", main);