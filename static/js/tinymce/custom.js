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
        content: `
            <p>
                The early childhood years are a very special time in your child's development. Great changes occur in this short
                period of time as children learn to communicate, increase their intellectual awareness and make great physical strides.
            </p>
            <p>
                At the Village Childcare Center, we use the Reggio Emilia approach to learning. This approach is a student-centered
                curriculum that uses self-directed, experiential learning in relationship-driven environments. This program is based on the
                principles of respect, responsibility and community learned through exploration, discovery and play. At the core of this
                philosophy is the assumption that children form their own personality during the early years of development and that they are
                endowed with "a hundred languages", through which they can express their ideas. The aim of the Reggio approach is to teach
                children how to use these symbolic languages, such as art, in everyday life. Using this philosophy ensures that no two classrooms
                will be the same. To implement this concept, our teachers will guide students to work on projects that emphasize the interest of
                the classroom rather than themes that do not benefit your child.
            </p>
            <p>
                Here at The Village, we choose to focus on each individuals' strengths rather than their weaknesses. Our childcare philosophy is to
                provide an age-appropriate environment that develops self-esteem, confidence, and love of learning. To create these conditions, we
                utilize our professionally educated staff and the materials to deliver an exceptional program to your child. Educationally, our goal
                is to foster a love of learning by integrating play and creativity into our curriculum. We challenge our students by promoting inquiry
                and encouraging discovery through exploring the world around them. This instills a sense of confidence in their ability to master new
                situations and tasks using their reasoning skills.
            </p>
            <p>
                You know your child best. We encourage you to contact the school about any questions or concerns you might have.
                We look forward to becoming a part of your child's community.
            </p>
        `,
    },
    classrooms: {
        title: `Classrooms`,
        content: `
            <h3>
                <strong>Newborn - 12 Months</strong>
            </h3>
            <p>
                Here, babies are made to feel safe, secure, and happy.
                This classroom gives warm, caring teachers an opportunity to
                bond and develop trust with little ones. Each child has a
                primary caregiver who will guide your child's development and
                be your main point of contact.
            </p>
            <p>
                In this classroom, children will enjoy a warm, nurturing classroom
                environment with stimulating activities and age-appropriate educational
                toys.
            </p>
            <h3>
                <strong>12 Months - 24 Months</strong>
            </h3>
            <p>
                These energetic little ones are growing and learning, so we channel their
                energy into positive learning moments by giving them ample room to move
                and explore. Here, toddlers receive encouragement and guidance toward the
                growth of their physical skills and emerging milestones:
            </p>
            <ul>
                <li>
                    Stimulating classroom environments
                </li>
                <li>
                    Milestone-based curriculum
                </li>
                <li>
                    Immersive learning experiences
                </li>
                <li>
                    Educational toys and activities
                </li>
            </ul>
            <p>
                Here, toddlers develop an understanding of their own feelings and
                relationship with people like family, friends, and community members;
                they also increase their ability to interact with others and develop
                self-awareness.
            </p>
            <h3>
                <strong>24 Months - 35 Months</strong>
            </h3>
            <p>
                This classroom is committed to potty training. A mobile, energetic
                2-year-old enjoys the entire world as their playground. We've put
                together a unique educational approach that focuses their enthusiasm
                into opportunities for development, growth, and achievement. Here,
                2-year-olds enjoy exclusive milestone-based curriculum and interactive,
                tactile learning experiences.
            </p>
            <p>
                Developing and understanding of their own emotions and their relationships
                with others, like family, friends, and community members, as well as
                understanding how to interact with others while developing self-awareness.
            </p>
        `,
        contentSecondary: `
            <h3>
                <strong>3 - 4 Year Olds</strong>
            </h3>
            <p>
                As they grow to be independent learners, these children develop the ability
                to work with others, follow directions, self-regulate, follow routines, and
                build self-help skills. This program offers:
            </p>
            <ul>
                <li>
                    Proprietary indicator-based curriculum
                </li>
                <li>
                    Opportunities to increase independence
                </li>
                <li>
                    Collaborative learning environments
                </li>
            </ul>
            <p>
                We will begin more projects in these classrooms- Children will be able to
                follow their strengths and imagination to explore the world around them.
            </p>
            <h3>
                <strong>Optional 4-year-old Preschool Program</strong>
            </h3>
            <p>
                In our preschool program our teachers will introduce interscope curriculum. Interscope
                curriculum offers additional resources designed to support daily learning. This includes
                strategies to individualize learning throughout the daily routine, as well as activities for building
                children's literacy skills and music to support learning. These resources are a first step in
                creating and engaging the rich learning environment that encourages young children to learn
                through exploration. Combined with diverse, open-ended materials that reflect children's home,
                language, and culture to provide an optimal learning environment that truly aligns with active
                learning.
            </p>
            <p>
                Our 4 year olds will have the opportunity to use the STEAM classroom from 9-12 Monday, Wed, Thursday.
                During this time, students will follow SCOPE curriculum. This program is also available to the public.
                The Village Childcare center will go in depth with the following:
            </p>
            <ul>
                <li>
                    <strong>Nature and Science:</strong> to comprehend the physical and natural world through observation, description, prediction, and data gathering.
                </li>
                <li>
                    <strong>Logic and Reasoning:</strong> Practicing sequencing, problem-solving, and critical thinking.
                </li>
            </ul>
        `,
    },
    steam: {
        title: `Science. Technology. Engineering. Art. Mathematics.`,
        content: `
            <img src="${django.staticPrefix + 'img/steam.png'}" class="school-img img-fluid rounded" />
            <h2>
                <strong class="text-primary">STEAM</strong> <strong>EDUCATION</strong>
            </h2>
        `,
        contentSecondary: `
            <p>
                Our S.T.E.A.M. classroom is designed to allow children to use their imagination to explore
                their creativity. Young children benefit from S.T.E.A.M. learning because they are generally
                naturally inquisitive and want to explore and make sense of themselves and the environment in
                which they live.
            </p>
            <p>
                In this classroom we will have professionals come on site weekly to teach children science,
                art, yoga, and music.
            </p>
            <p>
                <img src="${ django.staticPrefix + 'img/steam_art.png' }" alt="S.T.E.A.M. Art">
            </p>
        `,
    },
    preschool: {
        title: `Coming Fall 2023`,
        content: `
            <p>
                Our Preschool Program is an optional program as well as open to the public.
                In our preschool program our teachers will introduce interscope curriculum.
            </p>
            <p>
                <strong>Interscope curriculum</strong> offers additional resources designed to support daily learning. Includes
                strategies to individualize learning throughout the daily routine and
                activities for building children's literacy skills and music to support
                learning. These resources are a first step in creating and engaging the rich
                learning environment that encourages young children to learn through exploration.
                Combined with diverse, open-ended materials that reflect children's home, language,
                and culture to provide an optimal learning environment that truly aligns with active
                learning.
            </p>
            <p>
                Our 4 year olds will have the opportunity to use the STEAM classroom from 9-12 Monday,
                Wed, Thursday. During this time students will follow SCOPE curriculum. This program is
                also available to the public. The Village Childcare center will go in depth with the following:
            </p>
            <p>
                <strong>Nature and Science:</strong> to comprehend the physical and natural world through observation, description, prediction,
                and data gathering.
            </p>
            <p>
                <strong>Early Math:</strong> Learning about numbers, patterns, sorting, and ordering; learning to utilize numbers to add,
                subtract, measure, and graph.
            </p>
            <p>
                <strong>Logic and Reasoning:</strong> Practicing sequencing, problem-solving, and critical thinking.
            </p>
        `,
    },
    school_age: {
        title: `School Age`,
        content: `
            <h3>
                Before/After School Care
            </h3>
            <p>
                We know it can be stressful to find care for your children
                before and after school care. We offer care with Kalamazoo
                bus transportation. While your children are with us during
                this time, they will have the opportunity to relax, do homework,
                play outside, and play in our S.T.E.A.M room classroom.
            </p>
            <img src="${ django.staticPrefix + 'img/discover.png'}" alt="discover">
            <p>
                <strong>If there is a bus cancellation, we are unable to bus your child&nbsp;to&nbsp;school.</strong>
            </p>
        `,
        contentSecondary: `
            <h3>
                Summer Camp + School Breaks
            </h3>
            <p>
                This camp program is for elementary schoolers who are 5-12 years old. We guarantee
                your children will love spending their summers at the Village Childcare Center. We
                offer both onsite and offsite field trips. The spaces and activities are designed
                to be fun, engaging, and educational.
            </p>
            <p>
                No matter the weather, we will be enjoying the outdoors.
            </p>
            <img src="${ django.staticPrefix + 'img/explore1.png' }" alt="explore">
            <p>
                <strong>The Village Childcare Center follows KPS school schedule.</strong>
            </p>
        `,
    },
    contact: {
        title: `Contact Us`,
        content: `
            <h3>
                Schedule a tour
            </h3>
            <p>
                We strongly encourage parents to schedule a tour of the school. This will give you the
                opportunity to see the classrooms and witness first hand what your child can experience
                at The Village Childcare Center.
            </p>
            <p>
                If you have any questions, concerns, or wish to schedule a tour, please feel free to contact us.
            </p>
        `,
        contentSecondary: `
            <h3>
                Location:
            </h3>
            <ul>
                <li>
                    The Village Childcare Center
                </li>
                <li>
                    5320 Holiday Terrace
                </li>
                <li>
                    Kalamazoo, MI 49009
                </li>
            </ul>
            <ul>
                <li>
                    <strong>Local:</strong> (269) 253-8008
                </li>
                <li>
                    <strong>Fax:</strong> (269) 222-2588
                </li>
                <li>
                    <strong>Email:</strong> director@thevillageccc.com
                </li>
            </ul>
        `,
    },
}

const hasSecondaryContent = [
    'classrooms',
    'school_age',
    'contact',
    'steam',
]

/**
 * Show the secondary content for the page and update the title and content if set.
 * @param {bool} updateContent
 * @returns
 */
function showSecondaryContent(updateContent) {
    return () => {
        const $handleSelect = $('#id_handle');
        const handle = $handleSelect.val();
        if (!updateContent && handle) {
            $handleSelect.attr('disabled', true);
        }
        const $title = $('#id_title');
        const mceContent = tinymce.get("id_content");
        const $contentSecondary = $('.field-content_secondary');
        const mceContentSecondary = tinymce.get("id_content_secondary");

        if (updateContent) {
            mceContent.setContent(pageDefaults[handle].content);
        }
        $title.val(pageDefaults[handle].title);

        if (hasSecondaryContent.includes(handle)) {
            $contentSecondary.show();
            if (updateContent) {
                mceContentSecondary.setContent(pageDefaults[handle].contentSecondary);
            }
        } else {
            $contentSecondary.hide();
        }
    }
}

$(showSecondaryContent(false));
$('#id_handle').on('change', showSecondaryContent(true));
