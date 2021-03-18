function createCard(card) {
    if (!card.title) {
        card.title = "Empty card"
    }
    return `
        <div class="card" draggable="true" id="${card.id}" data-board-id='${card.board_id}' data-status='${card.status_id}'>
            <div class="card-remove"><i class="fas fa-trash-alt delete-card"></i></div>
            <div class="card-title">${card.title}</div>
        </div>
    `
}