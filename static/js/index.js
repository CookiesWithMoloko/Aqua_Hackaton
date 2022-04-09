$(function(){
    function onSearchHospital(e){
        $.get(`/searchhints/hospital/${e.target.value}`, function(data){
            let r = '';
            if (data.length == 0){
                r = `Ничего не найдено по запросу "${e.target.value}"`
                if (e.target.value.length <= 2){
                    return e.preventDefault();
                }
            }
            for (let i = 0; i < data.length; i++){
                r += `<li>${data[i]}</li>`;
            }
            e.target.parentElement.parentElement.children[1].classList.toggle('hidden', false);
            e.target.parentElement.parentElement.children[1].children[0].innerHTML = r;
        });
    }
    let e = $('#input_hospital')[0];
    e.addEventListener('input', onSearchHospital);
    e.addEventListener('focus', onSearchHospital);
    e.addEventListener('focusout', function(e){
        e.target.parentElement.parentElement.children[1].classList.toggle('hidden', true);
    })
})