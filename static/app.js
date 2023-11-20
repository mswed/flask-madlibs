const submitBtn = document.querySelector('button')

function notEmpty() {
    const inputs = document.querySelectorAll('input')
    const emptyInputs =  Array.from(inputs).every((field) => {
        return field.value.length > 0;
    })

    if (!emptyInputs) {
        alert('Ah... make sure you filled up all of the fields, ok?')
        return false;
    }

    return true;
}

submitBtn.addEventListener('click', (e) => {
    e.preventDefault()
    if (notEmpty()) {
        document.storyForm.submit();
    }
})
