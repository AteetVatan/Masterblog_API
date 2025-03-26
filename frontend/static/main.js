
//Global posts object
let globalPosts = [];

// Function that runs once the window is fully loaded
window.onload = function() {
    loadPosts();
    addEventListeners();
}

// Function to fetch all the posts from the API and display them on the page
function loadPosts() {
    console.log('loading posts');
    // Retrieve the base URL from the input field and save it to local storage
    var baseUrl = document.getElementById('api-base-url').value;
    const sortBy = document.getElementById('sort-by').value;
    const sortOrder = document.getElementById('sort-order').value;

    let sort_params = [];
    if (sortBy !== "") {
       sort_params.push("sort="+sortBy);
    }
    if (sortOrder !== "") {
       sort_params.push("direction="+sortOrder);
    }

    let query_string = "?" + sort_params.join("&")

    // Use the Fetch API to send a GET request to the /posts endpoint
    fetch(baseUrl + '/posts' + query_string)
        .then(response => response.json())  // Parse the JSON data from the response
        .then(data => {  // Once the data is ready, we can use it
            globalPosts = data;
            console.log("loadPosts received data:", data);
            // Clear out the post container first
            const postContainer = document.getElementById('post-container');
            postContainer.innerHTML = '';

            // For each post in the response, create a new post element and add it to the page
            data.forEach(post => {
                const postDiv = loadPostHTML(post);
                postContainer.appendChild(postDiv);
            });
        })
        .catch(error => console.error('Error:', error));  // If an error occurs, log it to the console
}


// Function to fetch all the posts from the API and display them on the page
function SearchPosts() {
    // Retrieve the base URL from the input field and save it to local storage
    const baseUrl = document.getElementById('api-base-url').value;
    const title = document.getElementById('search-post-title').value.trim();
    const content = document.getElementById('search-post-content').value.trim();

    if (title === "" && content === "") {
       alert("For Search Enter Title or Content sub string.");
       return;
    }

    let search_params = [];
    if (title !== "") {
       search_params.push("title="+title);
    }
    if (content !== "") {
       search_params.push("content="+content);
    }

    let query_string = "?" + search_params.join("&")
    console.log("SearchPosts with URL: ", baseUrl + '/posts/search' + query_string);
    // Use the Fetch API to send a GET request to the /posts endpoint
    fetch(baseUrl + '/posts/search' + query_string)
        .then(response => response.json())  // Parse the JSON data from the response
        .then(data => {  // Once the data is ready, we can use it
            console.log("SearchPosts received data:", data);

            // Clear out the post container first
            const postContainer = document.getElementById('post-container');
            postContainer.innerHTML = '';
            if (data.count > 0) {
                // For each post in the response, create a new post element and add it to the page
                data.results.forEach(post => {
                    const postDiv = loadPostHTML(post);
                    postContainer.appendChild(postDiv);
                });
            }else{
                postContainer.innerHTML = 'No posts with this search.'
            }

        })
        .catch(error => console.error('Error:', error));  // If an error occurs, log it to the console
}

function loadPostHTML(post) {
    let postDiv = document.createElement('div');
    postDiv.className = 'post';
    postDiv.id = 'post_' + post.post_id;
    postDiv.innerHTML = `
            <!-- DISPLAY MODE -->
            <div id="display_form_${post.post_id}" style="display:block;">
                <div class="post-buttons">
                    <button class="post-buttons-edit" onclick="toggleEditForm(${post.post_id})">Edit</button>
                    <button class="post-buttons-delete" onclick="deletePost(${post.post_id})">Delete</button>
                </div>
                <h2>${post.title}</h2>
                <p>${post.content}</p>
                <p><strong>Author:</strong> ${post.author || 'Anonymous'}</p>
                <p><strong>Notes:</strong> ${post.notes || 'None'}</p>
                <div class="post-buttons post-buttons-bottom">
                    <button type="button" class="like-btn update-btn" post_id="${post.post_id}" title="Like blog"></button>
                    <p id="like_count_p_${post.post_id}" style="${post.likes === 0 ? 'display: none;' : ''}">
                        <span class="span-like" id="like_count_span_${post.post_id}">${post.likes}</span> likes
                    </p>
                </div>
            </div>
            ` + editFormHTML(post);
    return postDiv;
}

function editFormHTML(post) {
    const isNew = !post;
    const postId = isNew ? 'new' : post.post_id;
    const title = isNew ? '' : post.title;
    const content = isNew ? '' : post.content;
    const author = isNew ? '' : post.author;
    const notes = isNew ? '' : post.notes;

    const cancelHandler = isNew
        ? 'hideADDPostForm()'
        : `cancelEdit(${postId})`;

    const formHTML = `
        <div id="edit_form_${postId}" class="edit-form" style="display:${isNew ? 'block' : 'none'};">
            <form onsubmit="submitEditForm(event, '${postId}')">
                <input type="text" name="title" title="Blog Title" placeholder="Blog Title"
                    value="${title}" required />
                <textarea name="content" rows="4" title="Content"
                    placeholder="Enter your Blog here..." required>${content}</textarea>
                <input type="text" name="author" title="Author" placeholder="Author"
                    value="${author}" />
                <input type="text" name="notes" title="Notes"
                    placeholder="Enter notes (optional)..." value="${notes}" />
                <div class="input-field">
                    <input type="submit" value="Save" />
                    <button class="edit-cancel" type="button" onclick="${cancelHandler}">Cancel</button>
                </div>
            </form>
        </div>
    `;
    return formHTML;
}

function addNewPostDisplay() {
    const addPostContainer = document.getElementById('add-post-container');
    addPostContainer.innerHTML = editFormHTML();
    addPostContainer.style.display = 'block';
}

function hideADDPostForm() {
    const addPostContainer = document.getElementById('add-post-container');
    addPostContainer.innerHTML = "";
    addPostContainer.style.display = 'none';
}


// Function to send a DELETE request to the API to delete a post
function deletePost(postId) {
    var baseUrl = document.getElementById('api-base-url').value;
    // Use the Fetch API to send a DELETE request to the specific post's endpoint
    fetch(baseUrl + '/posts/' + postId, {
        method: 'DELETE'
    })
    .then(response => {
        console.log('Post deleted:', postId);
        loadPosts(); // Reload the posts after deleting one
    })
    .catch(error => console.error('Error:', error));  // If an error occurs, log it to the console
}


function toggleEditForm(postId) {
    const displayDiv = document.getElementById(`display_form_${postId}`);
    const editDiv = document.getElementById(`edit_form_${postId}`);

    if (displayDiv.style.display === 'none') {
        displayDiv.style.display = 'block';
        editDiv.style.display = 'none';
    } else {
        displayDiv.style.display = 'none';
        editDiv.style.display = 'block';
    }
}

function cancelEdit(postId) {
    post = getPostById(postId);
    //Reset all fields
    populateDisplayForm(post)
    populateEditForm(post)
    toggleEditForm(postId);
}

function populateDisplayForm(post) {
  const display_id_prefix ='#display_form_' + post.post_id;
  document.querySelector(display_id_prefix + ' h2').textContent = post.title;
  document.querySelector(display_id_prefix + ' p:nth-of-type(1)').textContent = post.content;
  document.querySelector(display_id_prefix + ' p:nth-of-type(2)').innerHTML = '<strong>Author:</strong> ' + (post.author || 'Anonymous');
  document.querySelector(display_id_prefix + ' p:nth-of-type(3)').innerHTML = '<strong>Notes:</strong> ' + (post.notes || 'None');
}

function populateEditForm(post) {
  const edit_id_prefix ='#edit_form_' + post.post_id;
  document.querySelector(edit_id_prefix + ' input[name="title"]').value = post.title;
  document.querySelector(edit_id_prefix + ' textarea[name="content"]').value = post.content;
  document.querySelector(edit_id_prefix + ' input[name="author"]').value = post.author || '';
  document.querySelector(edit_id_prefix + ' input[name="notes"]').value = post.notes || '';
}

function submitEditForm(event, postId) {
    event.preventDefault();
    const form = event.target;
    const baseUrl = document.getElementById('api-base-url').value;

    const newPostData = {
        title: form.title.value.trim(),
        content: form.content.value.trim(),
        author: form.author.value.trim(),
        notes: form.notes.value.trim()
    };

    if (postId === 'new') {
        // Handle add logic here
        console.log("Creating new post:", newPostData);
         // Retrieve the values from the input fields


        // Use the Fetch API to send a POST request to the /posts endpoint
        fetch(baseUrl + '/posts', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(newPostData)
        })
        .then(response => response.json())  // Parse the JSON data from the response
        .then(post => {
            console.log('Post added:', post);
            hideADDPostForm();
            loadPosts(); // Reload the posts after adding a new one

        })
        .catch(error => console.error('Error:', error));  // If an error occurs, log it to the console
    } else {
        // Handle update logic
        console.log(`Updating post ${postId}`, newPostData);

        // Use the Fetch API to send a POST request to the /posts endpoint
        fetch(baseUrl + '/posts/' + postId, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(newPostData)
        })
        .then(response => response.json())  // Parse the JSON data from the response
        .then(post => {
            console.log('Post updated:', post);
            loadPosts(); // Reload the posts after adding a new one
        })
        .catch(error => console.error('Error:', error));  // If an error occurs, log it to the console
    }
}


// Function to send a POST request to the API to add a new post
function addPost() {
    // Retrieve the values from the input fields
    var baseUrl = document.getElementById('api-base-url').value;
    var postTitle = document.getElementById('post-title').value;
    var postContent = document.getElementById('post-content').value;

    // Use the Fetch API to send a POST request to the /posts endpoint
    fetch(baseUrl + '/posts', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: postTitle, content: postContent })
    })
    .then(response => response.json())  // Parse the JSON data from the response
    .then(post => {
        console.log('Post added:', post);
        loadPosts(); // Reload the posts after adding a new one
    })
    .catch(error => console.error('Error:', error));  // If an error occurs, log it to the console
}

function submitEdit(event, postId) {
    event.preventDefault();

    const form = event.target;
    const formData = {
        author: form.author.value,
        title: form.title.value,
        content: form.content.value,
        notes: form.notes.value
    };

    var baseUrl = document.getElementById('api-base-url').value;

    fetch(`${baseUrl}/posts/${postId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Post updated:', data);
        loadPosts();
    })
    .catch(error => console.error('Error:', error));
}

function getPostById(postId) {
    return globalPosts.find(p => p.post_id === postId);
}


function addEventListeners() {
    document.addEventListener('click', function(event) {
        if (event.target.classList.contains('like-btn')) {
            let postId = event.target.getAttribute('post_id');
            let baseUrl = document.getElementById('api-base-url').value;

            fetch(baseUrl + '/posts/update_likes', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ post_id: postId })
            })
            .then(response => response.json())
            .then(data => {
                let like_count_span = document.getElementById('like_count_span_' + data.post_id);
                if (like_count_span) {
                    like_count_span.innerText = data.likes;
                }
                let like_count_p = document.getElementById('like_count_p_' + data.post_id);
                if (like_count_p) {
                    if (data.likes > 0) {
                        like_count_p.style.display = "inline";
                    }else{
                        like_count_p.style.display = "none";
                    }
                }
            })
            .catch(error => console.error('Error:', error));
        }
    });
}
