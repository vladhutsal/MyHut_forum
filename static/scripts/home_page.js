const topicsContainer = document.getElementById('topics')
const topicSubmitForm = document.getElementById('newTopicForm')

topicSubmitForm.addEventListener('submit', createTopic)
getTopicsList(topicsContainer)


function getTopicsList(topicsEl) {
  handleRequest('api_topics/').then((data) => {
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
async function handleRequest(url, method, data) {
    const res = await fetch(url, method, data);
    const responseData = await res.json();
    return responseData;
}


generateTopicEl = (element) => {
  var generatedTopicEl = "<div class='col-12 mx-auto border py-3 mb-4'>\
  <h4><a href='topic/" + element.slug + "'>" + element.title + "</a></h4>\
  <p>" + element.text + "</p>\
  </div>"
  return generatedTopicEl
}


function createTopic(event) {
  event.preventDefault();
  const topicForm = event.target;
  const newFormData = new FormData(topicForm);

  handleRequest('api_topics/create', 'POST', newFormData)
    .then(response => {
        const status = response.status;
        const data = response.response;

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