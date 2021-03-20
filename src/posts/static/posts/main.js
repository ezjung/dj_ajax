'use strict';

console.log('hello World!')

const helloWorld = document.getElementById('hello-world');
const postsBox = document.getElementById('posts-box')
const spinnerBox = document.getElementById('spinner-box')

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

        setTimeout(() => {
            spinnerBox.classList.add('not-visible')
            console.log(data)

            data.forEach(el => {
                // postsBox.innerHTML += `
                //     ${el.title} - <b>${el.body}</b> - by ${el.author}<br>`
                // from 'cards'
                postsBox.innerHTML += `
                <div class="card mb-2">
                    <div class="card-body">
                        <h5 class="card-title">${el.title}</h5>
                        <p class="card-text">${el.body}</p>
                    </div>
                    <div class="card-footer">
                        <div class="row">
                        <div class="col-2">
                            <a href="#" class="btn btn-primary">Details</a>
                        </div>
                        <div class="col-2">
                            <a href="#" class="btn btn-primary">Like</a>
                        </div>       
                        </div>
                 
                    </div>
                </div>
                `
            });
        }, 1000)
        
    },
    error: function(error){
        console.log(error)
    },
})