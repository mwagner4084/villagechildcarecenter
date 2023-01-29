window.$ = django.jQuery;

/**
 * TinyMCE config settings
 * @typedef {import('tinymce').Settings} Settings
 */

/** @type {Settings} */
const settings = {
    selector: 'textarea[name^="content"]',
    height: "400",
    width: "100%",
    images_upload_url: '/upload_image/',
    convert_urls: false,
    plugins: "insertdatetime media image preview",
    toolbar: "undo redo |  bold italic | alignleft alignright aligncenter alignjustify | image media | preview",
    image_title: true,
    image_caption: true,
    // automatic_uploads: false,
    image_advtab: true,
    // file_picker_types: "image media",

    // file_picker_callback: function (cb, value, meta) {
    //   var input = document.createElement("input");
    //   input.setAttribute("type", "file");
    //   if (meta.filetype == "image") {
    //       input.setAttribute("accept", "image/*");}
    //   if (meta.filetype == "media") {
    //   input.setAttribute("accept", "video/*");}

    //   input.onchange = function () {
    //       var file = this.files[0];
    //       var reader = new FileReader();
    //       reader.onload = function () {
    //           var id = "blobid" + (new Date()).getTime();
    //           var blobCache =  tinymce.activeEditor.editorUpload.blobCache;
    //           var base64 = reader.result.split(",")[1];
    //           var blobInfo = blobCache.create(id, file, base64);
    //           blobCache.add(blobInfo);
    //          cb(blobInfo.blobUri(), { title: file.name });
    //        };
    //        reader.readAsDataURL(file);
    //    };
    //    input.click();
    // },
    content_style: "body { font-family:Helvetica,Arial,sans-serif; font-size:14px }",
    setup: function (editor) {
        editor.on('init', function (e) {
            console.log(e);
        });
    }
};

tinymce.init(settings);

const pageDefaults = {
    home: {
        title: `Opening Spring 2023`,
        content: `
            <p>
                Our mission is to provide child-centered care focused on fostering children's creativity, educational development,
                and independence. We provide a resource-rich, inclusive environment that allows each child to develop at his/her own pace.
                Our classrooms are designed to give children room to grow and express themselves in a safe space.
            </p>
            <img src="${django.staticPrefix + 'img/wander.jpeg'}" />
        `
    },
    philosophy: {
        title: `Welcome to the Village`,
        content: ``,
    },
    classrooms: {
        title: `Classrooms`,
        content: ``,
        contentSecondary: ``,
    },
    steam: {
        title: `Science. Technology. Engineering. Art. Mathematics.`,
        content: `
            <img src="${django.staticBase + 'img/steam.png'}" />
            <h2>
                <strong>STEAM</strong> <strong>EDUCATION</strong>
            </h2>
        `,
        contentSecondary: ``,
    },
    preschool: {
        title: `Coming Fall 2023`,
        content: ``,
    },
    school_age: {
        title: `School Age`,
        content: ``,
        contentSecondary: ``,
    },
    contact: {
        title: `Contact Us`,
        content: ``,
        contentSecondary: ``,
    },
}

$('#id_handle').on('change', (e) => {
    const handle = e.target.value;
    const $title = $('#id_title');
    const mceContent = tinymce.get("id_content");
    const $contentSecondary = $('.field-content_secondary');
    const mceContentSecondary = tinymce.get("id_content_secondary");

    mceContent.setContent(pageDefaults[handle].content);
    $title.val(pageDefaults[handle].title);

    if (handle === 'classrooms' || handle === 'school_age' || handle === 'contact' || handle === 'steam') {
        $contentSecondary.show();
        mceContentSecondary.setContent(pageDefaults[handle].contentSecondary);
    } else {
        $contentSecondary.hide();
    }
});
