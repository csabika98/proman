import { dom } from "./dom.js";

// This function is to initialize the application
init();

function pageLoad(){
    return new Promise((resolve,reject)=>{
        //here our function should be implemented 
        setTimeout(()=>{
            resolve();
        ;} , 1000
        );
    });
}
async function init() {
    // init data
    dom.init();
    // loads the boards to the screen
    dom.loadBoards(); //load empty board with unique id's from api
    dom.loadStatuses(); // initialize the status bars
    await pageLoad();
    dom.loadCards(); // load cards for each status in each unique boards with given id's
}



