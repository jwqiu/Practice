// function handleSubmit(event) {

//     event.preventDefault();  // 阻止表单的默认提交行为

//     // 显示弹窗提示
//     const popup = document.getElementById('popup');
//     popup.style.display = "block";

//     // 2秒后自动隐藏弹窗
//     setTimeout(function() {
//         popup.style.display = "none";
//         event.target.submit();  // 手动提交表单，页面刷新
//     }, 3000);

// }

// 获取所有以 'delete-' 开头的表单
var deleteForms = document.querySelectorAll('form[id^="delete-"]');

deleteForms.forEach(function(form) {
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        alert('删除成功');

        // 使用 setTimeout 延迟提交，避免递归
        setTimeout(function() {
            form.submit(); // 手动提交表单
        }, 0);
    });
});