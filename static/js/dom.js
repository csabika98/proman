// It uses data_handler.js to visualize elements
import { dataHandler } from "./data_handler.js";

export let dom = {
    init: function () {

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
        
        let container = document.createElement('div')
        container.classList.add('container')


        //create the empty boards with clean structure and branching
        for(let board of boards){
            //console.log('board id: ' + board.id)
            //let addButton = document.createElement('button')
            let minimizeButton = document.createElement('button')
            let renameForm = document.createElement("form")
            let renameInput = document.createElement("input")
            let renameSubmit = document.createElement("button")
            renameSubmit.setAttribute("type", "submit")
            renameSubmit.setAttribute("value", "Submit")
            renameSubmit.classList.add("btn","btn-primary")
            renameSubmit.textContent = "Submit"
            renameForm.setAttribute("method","post")
            renameForm.setAttribute("action",`/rename-board/${board.id}`)
            renameInput.setAttribute("type", "text")
            renameInput.classList.add('Input-text')
            renameInput.setAttribute('placeholder', 'Rename board')
            renameInput.setAttribute("id", "rename")
            renameInput.setAttribute("name", "rename")
            renameSubmit.setAttribute("type", "submit")
            renameForm.appendChild(renameInput)
            renameForm.appendChild(renameSubmit)
            let title = document.createElement('div')
            let title_and_butttonDiv = document.createElement('div')
            let Icon = document.createElement('i')
            let boardpanel = document.createElement('div')
            let header = document.createElement('div')
            let body = document.createElement('div')
            let bodyContent = document.createElement('div')
            let newCard = document.getElementById("addcard")
            let newForm = document.createElement("form")
            let newInput = document.createElement("input")
            let newButton = document.createElement("button")

            newCard.addEventListener("click", function(){
                newForm.setAttribute("method","post")
                newForm.setAttribute("action",`/new-card/${board.id}`)
                newForm.setAttribute("data-board-id",`${board.id}`)
                newInput.setAttribute("type","text")
                newInput.classList.add('Input-text')
                newInput.setAttribute('placeholder', 'Name of the card')
                newInput.setAttribute("id", "newcard")
                newInput.setAttribute("board-id", `${board.id}`)
                newInput.setAttribute("name", "newcard")
                newButton.setAttribute("type","submit")
                newButton.classList.add("btn","btn-primary")
                newButton.textContent = "Submit"
                newForm.appendChild(newInput)
                newForm.appendChild(newButton)


            })
            
            bodyContent.classList.add('row')

            Icon.classList.add('fas','fa-caret-down')
            //addButton.classList.add('btn','btn-primary', 'btn-sm')
            minimizeButton.classList.add('btn','btn-primary', 'btn-sm')
            $(minimizeButton).click(function() {
                $(header).click(function() {
                    $(this).next().toggle();
                    return false;
                }).next().hide();
              });
            //addButton.textContent = 'Add card'
            //addButton.setAttribute('data-board', board.id)
            bodyContent.id = 'cardContent'
            body.classList.add('card-body')
            header.classList.add('card-header', 'd-flex', 'justify-content-between')
            boardpanel.classList.add('card')
            
            title.textContent = board.title
            minimizeButton.append(Icon)
            header.setAttribute('id','header')
            title.setAttribute('contenteditable', true)
            boardpanel.setAttribute('id',board.id)
            boardpanel.setAttribute('name','board')
         
            body.append(bodyContent)

            header.append(title,minimizeButton,renameForm)
            boardpanel.append(newForm,header,body)
            container.append(boardpanel)
            }

        let boardsContainer = document.querySelector('#boards');
        boardsContainer.append(container)
    },

    loadCards: function () {
        //load cards from datahandler with the api form route /get-cards
        dataHandler.getAllCards(function(cards){
            dom.showCards(cards)
        })
        
    },

    showCards: function (cards) {
        // shows the cards of a board
        // it adds necessary event listeners also
        let cardContent = document.querySelectorAll('[name=board]')
        for(let board of cardContent){

            let newStatus = board.querySelectorAll('[id=new]')[0];
            let progressStatus = board.querySelectorAll('[id="inProgress"]')[0];
            let testingStatus = board.querySelectorAll('[id="testing"]')[0];
            let doneStatus = board.querySelectorAll('[id="done"]')[0];

            for(let card of cards){
                if(board.id == card.board_id){
                    if(card.status_id==0){
                        let cardDiv = document.createElement('li')
                        cardDiv.classList.add('card')
                        cardDiv.id = 'interactiveCard'
                        cardDiv.append(card.title)

                        $(cardDiv).draggable({
                            snap: true,
                            helper: 'clone',
                            zIndex: 1000,
                            revert: "invalid",
                            containment:"document"
                        });
                        
                        $('ul[name="dropable"]').droppable({
                            drop:function(event, ui) {
                                ui.draggable.detach().appendTo($(this));
                            }
                        });

                        //$(cardDiv).attr('contenteditable','true');
                        newStatus.append(cardDiv)
                    }
                    else if(card.status_id==1){
                        let cardDiv = document.createElement('li')
                        cardDiv.classList.add('card')
                        cardDiv.id = 'interactiveCard'
                        cardDiv.append(card.title)

                        $(cardDiv).draggable({
                            snap: true,
                            helper: 'clone',
                            zIndex: 1000,
                            revert: "invalid",
                            containment:"document"
                        });
                        
                        $('ul[name="dropable"]').droppable({
                            drop:function(event, ui) {
                                ui.draggable.detach().appendTo($(this));
                            }
                        });

                        //$(cardDiv).attr('contenteditable','true');
                        progressStatus.append(cardDiv)
                    }
                    else if(card.status_id==2){
                        let cardDiv = document.createElement('li')
                        cardDiv.classList.add('card')
                        cardDiv.id = 'interactiveCard'
                        cardDiv.append(card.title)

                        $(cardDiv).draggable({
                            snap: true,
                            helper: 'clone',
                            zIndex: 1000,
                            revert: "invalid",
                            containment:"document"
                        });
                        
                        $('ul[name="dropable"]').droppable({
                            drop:function(event, ui) {
                                ui.draggable.detach().appendTo($(this));
                            }
                        });
                    
                        //$(cardDiv).attr('contenteditable','true');
                        testingStatus.append(cardDiv)
                    }
                    else if(card.status_id==3){
                        let cardDiv = document.createElement('li')
                        cardDiv.classList.add('card')
                        cardDiv.id = 'interactiveCard'
                        cardDiv.append(card.title)

                        $(cardDiv).draggable({
                            snap: true,
                            helper: 'clone',
                            zIndex: 1000,
                            revert: "invalid",
                            containment:"document"
                        });
                        
                        $('ul[name="dropable"]').droppable({
                            drop:function(event, ui) {
                                ui.draggable.detach().appendTo($(this));
                            }
                        });

                        //$(cardDiv).attr('contenteditable','true');
                        doneStatus.append(cardDiv)
                    }
                }
            }
        }

    },

    loadStatuses: function(statuses){
        dataHandler.getStatuses(function(statuses){
            dom.showStatuses(statuses);
        });
    },
    
    showStatuses: function(status){
        let cardContent = document.querySelectorAll('[id=cardContent]')
        let statusNames = [
            'New',
            'In progress',
            'Testing',
            'Done'
        ];

        for(let card of cardContent){
            for(let i=0;i<status.length;i++){
                let stat = document.createElement('ul')
                stat.classList.add('col', 'card', 'text-center')
                stat.textContent = statusNames[i]
                stat.setAttribute('name','dropable')
                stat.id = status[i]['title']

                card.append(stat)
            }
        }
    }
}