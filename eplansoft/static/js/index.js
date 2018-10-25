// Self invoking function to not conflict with global variables in base; using a closure
(() => {
    const form = document.querySelector("[data-js=form]");


    form &&
        form.addEventListener("submit", event => {
            // event.preventDefault();

            // results.style.display = "block";

            // const fileNameValue = fileNameField.value;

            // const span = document.createElement("span");
            // span.innerText = fileNameValue;

            // fileName.appendChild(span);
        });
})();