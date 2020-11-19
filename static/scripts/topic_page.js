const { handleRequest } = require('./home_pagehome_page.js');


async function handleLikes(event, commentId) {
    const action = event.target.value;
    const url = `api/comments/${commentId}/like`;
    const res = await handleRequest(url, JSON.stringify(action));
    console.log(res)
}
