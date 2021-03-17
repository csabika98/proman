// It uses data_handler.js to visualize elements
import { dataHandler } from "./data_handler.js";

export let dom = {
    init: function () {
        // This function should run once, when the page is loaded.
    },
    loadBoards: function () {
        // retrieves boards and makes showBoards called
        dataHandler.getBoards(function(boards){
            dom.showBoards(boards);
        });
    },
    showBoards: function (boards) {
        // shows boards appending them to #boards div
        // it adds necessary event listeners also

        let containter = document.createElement('div')
        containter.classList.add('container')

        for(let board of boards){
            let row = document.createElement('div')
            row.classList.add('row');

            let panel = document.createElement('section')
            panel.classList.add("card-panel");
            panel.textContent = board.title;

            let boardsContainer = document.querySelector('#boards');
            boardsContainer.classList.add('container')
            row.append(panel);
            boardsContainer.append(row);

        }

    },
    loadCards: function (boardId) {
        // retrieves cards and makes showCards called
    },
    showCards: function (cards) {
        // shows the cards of a board
        // it adds necessary event listeners also
    },
    // here comes more features
};
