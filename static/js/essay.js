
$(document).ready(function(){

        tinymce.init({
        selector:'div#blog_article',
        theme: "modern",
        language: "zh_CN",
        height: 600,
        plugins: [
            'advlist autolink lists link image charmap print preview hr anchor pagebreak',
            'searchreplace wordcount visualblocks visualchars code fullscreen',
            'insertdatetime media nonbreaking save table contextmenu directionality',
            'emoticons template paste textcolor colorpicker textpattern imagetools codesample toc'
        ],
        toolbar1: 'undo redo | insert | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image',
        toolbar2: 'print preview media | forecolor backcolor emoticons | codesample',
        image_advtab: true,
        templates: [
            { title: 'Test template 1', content: 'Test 1' },
            { title: 'Test template 2', content: 'Test 2' }
        ],
        content_css: [
            '//fonts.googleapis.com/css?family=Lato:300,300i,400,400i',
            '//www.tinymce.com/css/codepen.min.css'
        ]
    });

});

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$('#submit').click(function(){

    var _xsrf = getCookie('_xsrf');
    var blog_title = $('#blog_title').val();
    var blog_article=tinymce.get('blog_article').getContent();
    $.ajax({
        url:'/essay_upload',
        type:'post',
        data:{
            blog_title:blog_title,
            blog_article:blog_article,
            _xsrf:_xsrf
        },
        dataType:'json',
        success:function(data){
            if(data['status'] == 'true'){
                url = "/essay_upload_status?status=上传成功";
                url += "&blog_uuid="+data['blog_uuid'];
                location.href = url;
            }else{
                alert('上传失败,请重新上传');
            }
        },
        error:function(){
            alert('error');
        }
    });
});

