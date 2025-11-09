fetch('/cat')
    .then(res => res.json())
    .then(data => document.getElementById('fact').innerText = data.fact);
