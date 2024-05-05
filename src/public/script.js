(function main() {
    const form = document.getElementById("nyoklat__form");
    const imageDisplayerShadow = document.getElementsByClassName("imageDisplay__shadow")[0]
    const imageDisplayerCaption = document.getElementsByClassName("imageDisplay__caption")[0]
    const resetButton = document.getElementById("form__reset");
    const imageDisplayer = document.getElementById("form__displayCanvas")

    // Refresh
    form.reset();

    resetButton.addEventListener("click", e => {
        const ctx = imageDisplayer.getContext("2d")

        ctx.clearRect(0, 0, imageDisplayer.width, imageDisplayer.height)
        imageDisplayerShadow.style.display = "block";
        imageDisplayerCaption.style.display = "block"
        document.getElementById("form__imageInput").value = null
    });

    imageDisplayerShadow.addEventListener("click", (e) => {
        document.getElementById("form__imageInput").click()
    })

    form.addEventListener("change", (e) => {
        // Ref: https://stackoverflow.com/questions/63151823/how-to-display-a-picture-from-file-input-to-canvas
        const ctx = imageDisplayer.getContext("2d")
                                    
        const image = new Image();
        image.src = URL.createObjectURL(e.target.files[0]);
        image.onload = function() {
            ctx.drawImage(image, 0, 0,
                imageDisplayer.width, imageDisplayer.height
            )
        }

        imageDisplayerShadow.style.display = "none";
        imageDisplayerCaption.style.display = "none";
    })

    form.addEventListener("submit", async(e) => {
        e.preventDefault();
        const resultDisplay = document.getElementById("nyoklat__result")
        resultDisplay.textContent = "Hasil sedang diproses!"

        const formData = new FormData(e.target);
        await fetch("/predict", {
                method: "POST",
                body: formData,
            })
            .then(res => res.json())
            .then(res => {
                if(res.detail != "success") {
                    let errMsg;
                    switch(res.detail) {
                        case "no_image":
                            errMsg = "No image being supplied"
                            break;
                    }
                    throw new Error(errMsg);
                }
                
                resultDisplay.textContent = res.prediction;
            })
            .catch(err => {
                resultDisplay.innerHTML = `Failed! Please try again <br> Reason: ${err.message}`
            })
    })

})()