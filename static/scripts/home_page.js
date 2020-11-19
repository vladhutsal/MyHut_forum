const topicsContainer = document.getElementById('topics');
const topicSubmitForm = document.getElementById('newTopicForm');

topicSubmitForm.addEventListener('submit', createTopic);
getTopicsList(topicsContainer);


async function getTopicsList(topicsEl) {
  const response = await handleRequest('api/topics/');
  const data = response.resData;
  let finalTopic = "";

  for (let i=0; i<data.length; i++) {
    currentEl = generateTopicEl(data[i]);
    finalTopic += currentEl;
    }

  topicsEl.innerHTML = finalTopic;
  return;
}


async function createTopic(event) {
  event.preventDefault();
  const newFormData = new FormData(event.target);
  const newTopicObj = {
    title: newFormData.get('title'),
    text: newFormData.get('text')
  }

  const requestData = {
    method: 'POST',
    body: JSON.stringify(newTopicObj),
    headers: {
      'Content-type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken')
    }};

  const response = await handleRequest('api/topics/create', requestData);
  const status = response.status;
  const data = response.resData;
    if (![201, 200].includes(status)) {
      console.error({status, message: 'Something unexpected happened'});

    } else {
      const newTopicEl = generateTopicEl(data);
      const topicsList = topicsContainer.innerHTML;
      topicsContainer.innerHTML = newTopicEl + topicsList;
    
      event.target.reset();
    };
}


// lets make requests with fetch method, not xhr
async function handleRequest(url, reqData) {

    const res = await fetch(url, reqData);
    const status = res.status;
    const resData = await res.json();
    return {status, resData};
}


generateTopicEl = (element) => {
  let generatedTopicEl = "<div class='col-12 mx-auto border py-3 mb-4'>\
  <h4><a href='topic/" + element.id + "'>" + element.title + "</a></h4>\
  <p>" + element.text + "</p>\
  </div>"
  return generatedTopicEl;
}


function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}