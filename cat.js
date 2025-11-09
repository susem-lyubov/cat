fetch('https://cat-9x4s.onrender.com/cat')
    .then(res => res.json())
    .then(data => document.getElementById('fact').innerText = data.fact);
