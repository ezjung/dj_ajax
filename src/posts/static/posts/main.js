console.log('hello World!')

const helloWorld = document.getElementById('hello-world')

// helloWorld.textContent = "Mochi Muffins"
helloWorld.innerHTML = "Mochi <b>Muffins</b>"

$.ajax({
    type: 'GET',
    url: '/hello/',
    success: function(response){
        console.log('success', response.text)
        helloWorld.textContent = response.text
    },
    error: function(error){
        console.log('error', error)
    }
})