const input = document.querySelector("#keywords");
console.log(url);
input.addEventListener("focus", (e) => {
  fetch(url, {
    method: "GET",
  })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
    });
});
