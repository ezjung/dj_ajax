'use strict';

console.log('hello World!')

const helloWorld = document.getElementById('hello-world');
const postsBox = document.getElementById('posts-box')

// helloWorld.textContent = "Mochi Muffins"
// helloWorld.innerHTML = "Mochi <b>Muffins</b>"

$.ajax({
    type: 'GET',
    url: '/hello/',
    success: function(response){
        console.log('success', response.text);
        helloWorld.textContent = response.text;
    },
    error: function(error){
        console.log('error', error);
    },
})

$.ajax({
    type: 'GET',
    url: '/data/',
    success: function(response){
        console.log(response);
        // const data = JSON.parse(response.data);
        // console.log(data);
        const data = response.data
        console.log(data)

        data.forEach(el => {
            postsBox.innerHTML += `
                ${el.title} - <b>${el.body}</b> - by ${el.author}<br>
            `
        });
    },
    error: function(error){
        console.log(error)
    },
})