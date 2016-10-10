const listOfSentences = document.getElementByID('leste');
const addButton = document.getElementByID('create');
const removeButton = document.getElementByID('remove');

addButton.addEventListener('click', function () {
  const svadaSentence = createSvadaSentence()
  addSentenceToList(svadaSentence);
})

removeButton.addEventListener('click', function () {
  removeLastSentenceFromList();
})

function addSentenceToList(sentence) {
  const listElement = document.createElement('li');
  const sentenceNode = document.createTextNode(sentence);
  listElement.appendChild(sentenceNode);
  listOfSentences.appendChild(listElement);
}

function removeLastSentenceFromList() {
  const listElements = listOfSentences.childNodes();
  if (listElements.length) {
    const lastListElement = listElements[listElements.length -1];
    listOfSentences.removeChild(lastListElement);
  }
}
  
function randomNumber() {
  return Math.floor(Math.random() * 3)
}
