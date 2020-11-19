const topicsContainer = document.getElementById('topics')
const topicSubmitForm = document.getElementById('newTopicForm')

topicSubmitForm.addEventListener('submit', createTopic)
getTopicsList(topicsContainer)


function getTopicsList(topicsEl) {
  handleRequest('api/topics/').then((data) => {
    console.log(data)

    let finalTopic = "";

    for (var i=0; i<data.length; i++) {
      currentEl = generateTopicEl(data[i]);
      finalTopic += currentEl;
      }

    topicsEl.innerHTML = finalTopic;
  });

  return;
}


// lets make requests with fetch method, not xhr
async function handleRequest(url, data) {
    console.log(data)
    const res = await fetch(url, data);
    const responseData = await res.json();
    return responseData;
}


generateTopicEl = (element) => {
  var generatedTopicEl = "<div class='col-12 mx-auto border py-3 mb-4'>\
  <h4><a href='topic/" + element.id + "'>" + element.title + "</a></h4>\
  <p>" + element.text + "</p>\
  </div>"
  return generatedTopicEl
}


function createTopic(event) {
  event.preventDefault();
  const newFormData = new FormData(event.target);
  const data = {
    title: newFormData.get('title'),
    text: newFormData.get('text')
  }

  handleRequest('api/topics/create', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken')
    },
  }).then(response => {
        console.log(response)

  // early return method, easier to look at the code
  if (![201, 200].includes(status)) {
    console.error({status, data, message: 'Something unexpected happened'});

    return;
  }

  const newTopic = generateTopicEl(data);
  const topic = topicsContainer.innerHTML;
  topicsContainer.innerHTML = newTopic + topic;

  console.log(data);

  topicForm.reset();
  })
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