<script>
document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("mailForm");

    if (!form) {
        console.log("Form not found");
        return;
    }

    form.addEventListener("submit", async function(e) {
        e.preventDefault();

        const sender = document.getElementById("sender").value;
        const receiver = document.getElementById("receiver").value;
        const message = document.getElementById("message").value;

        try {
            const response = await fetch("http://127.0.0.1:8000/send-mail", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    sender: sender,
                    receiver: receiver,
                    message: message
                })
            });

            const data = await response.json();
            alert(data.message);

        } catch (error) {
            alert("Server not running or connection error");
            console.error(error);
        }
    });
});
</script>
