function FinishAttempt(){
    var count_of_questions = document.getElementsByClassName('question-card').length;
    var inputOfAnswers = document.getElementById('answers');
    var options = document.getElementsByClassName('form-check-input');
    var selected_options = 0;
    for(var i = 0; i < options.length; i++){
        if(options[i].checked){
            selected_options++;
            inputOfAnswers.value += options[i].value + " ";
        }
    }
    
    if(selected_options != count_of_questions){
        return alert("Siz hali barcha savollarga javoblarni belgilamadingiz");
    }

    else{
        const sendFormButton = document.querySelector("#sendForm");
        sendFormButton.innerHTML="Yuborilmoqda ...";
        sendFormButton.setAttribute("disabled", "");
        document.getElementById("answersForm").submit();
    }
}