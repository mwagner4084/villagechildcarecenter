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
    valid_elements: "*[*]",
    images_upload_url: '/upload_image/',
    convert_urls: false,
    plugins: "insertdatetime media image preview code",
    toolbar: "undo redo | code | formatselect | bold italic | alignleft alignright aligncenter alignjustify | image media | preview",
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

/* Default template content */
const pageDefaults = {
    home: {
        title: `Now Enrolling for Fall!`,
        content: `
            <h3>
                Our Mission
            </h3>
            <p>
                Our mission is to provide child-centered care focused on fostering children's creativity, educational development, and independence. We provide a resource-rich, inclusive environment that allows each child to develop at his/her own pace. Our classrooms are designed to give children room to grow and express themselves in a safe space.
            </p>
            <p>
                <img src="${django.staticPrefix + 'img/wander.jpeg'}" />
            </p>
        `,
        contentSecondary: `
            <h3>
                Learn more about our...
            </h3>
            <p>
                <i class="bi bi-rainbow"></i>
                <a href="/classrooms">
                    Classrooms
                </a>
                <br>
                <i class="bi bi-boxes"></i>
                <a href="/preschool">
                    Preschool Program
                </a>
                <br>
                <i class="bi bi-shop"></i>
                <a href="/school-age">
                    School Age Programs
                </a>
                <br>
                <i class="bi bi-palette-fill"></i>
                <a href="/steam">
                    S.T.E.A.M. Room
                </a>
            </p>
        `,
    },
    philosophy: {
        title: `Welcome to the Village`,
        content: `
            <p>
                Early childhood is a very special time in your child's development. Great changes occur in this short period of time as children learn to communicate, increase their intellectual awareness, and make great physical strides.
            </p>
            <p>
                At the Village Childcare Center, we use the Reggio Emilia approach to learning. This approach is a student-centered curriculum that uses self-directed, experiential learning in relationship-driven environments. This program is based on the principles of respect, responsibility, and community learned through exploration, discovery, and play. At the core of this philosophy is the assumption that children form their own personality during the early years of development and that they are endowed with "a hundred languages", through which they can express their ideas. The aim of the Reggio approach is to teach children how to use these symbolic languages, such as art, in everyday life. Using this philosophy ensures that no two classrooms will be the same. To implement this concept, our teachers will guide students to work on projects that emphasize the interest of the classroom rather than themes that do not benefit your child.
            </p>
            <p>
                Here at The Village, we choose to focus on each individual's strengths rather than their weaknesses. Our childcare philosophy is to provide an age-appropriate environment that develops self-esteem, confidence, and a love of learning. To create these conditions, we utilize our professionally educated staff and the materials to deliver an exceptional program to your child. Educationally, our goal is to foster a love of learning by integrating play and creativity into our curriculum. We challenge our students by promoting inquiry and encouraging discovery through exploring the world around them. This instills a sense of confidence in their ability to master new situations and tasks using their reasoning skills.
            </p>
            <p>
                You know your child best. We encourage you to contact the school about any questions or concerns you might have. We look forward to becoming a part of your child's community.
            </p>
        `,
        accordion: `
            <p>
                We are dedicated to giving children a love of learning in a safe and secure environment. Our teachers design their own lesson plans to help children learn and explore the world at their own pace. Our teachers are loving, nurturing, trained professionals committed to maintaining the highest quality in early childhood education. Through onsite training provided by the Director, our teachers receive ongoing training in order to learn the latest developments within the field of Early Childhood Education.
            </p>
            <p>
                The Village is a safe, secure, clean, and happy environment for children to grow and learn. Each child is treated as a unique individual. They are given individual attention within a group, allowing them to develop according to their own needs and rate of development. Our number one priority is providing every child with a loving and caring atmosphere that encourages the development of self-esteem, confidence, creativity, and a love of learning.
            </p>
        `,
        accordionSecondary: `
            <ul>
                <li>
                    Every child in our program has the right to be respected as an individual with concern for his or her own interests, handicaps, special talents, and individual style and pace of learning.
                </li>
                <li>
                    Every child has the right to a calm, warm, loving, and nurturing environment where physical attention (hugs and cuddling) is freely given so that a child feels valued and secure and thus able to develop positive self-esteem.
                </li>
                <li>
                    Every child has the right to personal attention, a relaxed atmosphere, and freedom of choice in their daily activities.
                </li>
                <li>
                    Every child has the right to have all physical needs met, including the need for rest and relaxation throughout the day.
                </li>
                <li>
                    Every child has the right to experience various activities throughout the day that help them develop independence and confidence.
                </li>
                <li>
                    These activities provide opportunities for creativity, exploration, learning, and development in language skills, gross and fine motor skills, cognitive skills, social skills, and emotional/psychological development.
                </li>
            </ul>
        `,
    },
    classrooms: {
        title: `Classrooms`,
        content: `
            <h4>
                <strong>Newborn - 12 Months</strong>
            </h4>
            <p>
                Here, babies are made to feel safe, secure, and happy. This classroom gives warm, caring teachers an opportunity to bond and develop trust with little ones. Each child has a primary caregiver who will guide your child's development and be your main point of contact.
            </p>
            <p>
                In this classroom, children will enjoy a warm, nurturing classroom environment with stimulating activities and age-appropriate educational toys.
            </p>
            <h4>
                <strong>12 Months - 30 Months</strong>
            </h4>
            <p>
                These energetic little ones are growing and learning, so we channel their energy into positive learning moments by giving them ample room to move and explore. Here, toddlers receive encouragement and guidance toward the growth of their physical skills and emerging milestones:
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
                Here, toddlers develop an understanding of their own feelings and relationships with people like family, friends, and community members; they also increase their ability to interact with others and develop self-awareness.
            </p>
        `,
        contentSecondary: `
            <h4>
                <strong>30 Months - 40 Months</strong>
            </h4>
            <p>
                This classroom is committed to potty training. A mobile, energetic 2-year-old enjoys the entire world as their playground. We've put together a unique educational approach that focuses their enthusiasm on opportunities for development, growth, and achievement. Here, 2-year-olds enjoy an exclusive milestone-based curriculum and interactive, tactile learning experiences.
            </p>
            <p>
                We will focus on developing an understanding of their own emotions and their relationships with others, like family, friends, and community members, as well as understanding how to interact with others while developing self-awareness.
            </p>
            <h4>
                <strong>3 - 4 Year Olds</strong>
            </h4>
            <p>
                As they grow to be independent learners, these children develop the ability to work with others, follow directions, self-regulate, follow routines, and build self-help skills. This program offers:
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
                We will begin more projects in these classrooms - children will be able to follow their strengths and imagination to explore the world around them.
            </p>
        `,
        accordion: `
            <p>
                The Village faculty is eager to share in the process of potty training. Our official potty-training age is 24-36 months. At this age, our classroom faculty works diligently with the children to promote using the toilet. We do realize that some children begin training at younger ages. In these cases, our faculty will work with your child on a more individual basis to reinforce procedures that you are using at home.
            </p>
            <p>
                Your child may be ready for potty training if:
            </p>
            <ol>
                <li>
                    They have a dry diaper for two hours or more.
                </li>
                <li>
                    They have dry diapers after naptime.
                </li>
                <li>
                    They tell you when their diaper needs to be changed.
                </li>
                <li>
                    They tell you when they are urinating or making a bowel movement in their diaper.
                </li>
                <li>
                    They show an interest or curiosity in using the toilet.
                </li>
            </ol>
            <p>
                As your child is beginning to potty train, we suggest heavy cotton training pants or rubber pants which may be more effective than pull-ups. Rubber pants keep their clothes dry. Cotton pants may leave your child feeling a bit uncomfortable so they will quickly learn to relieve themselves using the toilet. Pull-ups are most effective AFTER the child has shown that they are dry most of the time or at bedtime.
            </p>
            <p>
                Please remind your child to go to the potty at home. When he or she is successful, use positive reinforcement.
            </p>
            <p>
                It is not recommended that your child be allowed to wear underpants over diapers or pull-ups. This defeats the purpose of them and removes the incentive for your child to wear underwear. Lastly, it is important to be consistent in whichever method you choose to use.
            </p>
        `,
    },
    steam: {
        title: `S.T.E.A.M. Room`,
        content: `
            <img src="${django.staticPrefix + 'img/steam.png'}" class="school-img img-fluid rounded" />
            <h2>
                <strong class="text-primary">STEAM</strong> <strong>EDUCATION</strong>
            </h2>
        `,
        contentSecondary: `
            <p>
                Our S.T.E.A.M. classroom is designed to allow children to use their imagination to explore their creativity. Young children benefit from S.T.E.A.M. learning because they are generally naturally inquisitive and want to explore and make sense of themselves and the environment in which they live.
            </p>
            <p>
                In this classroom, we will have professionals come on-site weekly to teach children science, art, yoga, and music.
            </p>
        `,
    },
    preschool: {
        title: `Now Enrolling for Fall!`,
        content: `
            <p>
                Our Preschool Program is an optional program as well as open to the public. In our preschool program, our teachers will introduce highscope curriculum.
            </p>
            <p>
                <strong>Highscope curriculum</strong> offers additional resources designed to support daily learning. This includes strategies to individualize learning throughout the daily routine and activities for building children's literacy skills and music to support learning. These resources are the first step in creating and engaging a rich learning environment that encourages young children to learn through exploration. Combined with diverse, open-ended materials that reflect children's home, language, and culture to provide an optimal learning environment that truly aligns with active learning.
            </p>
            <p>
                Our 4-year-olds will have the opportunity to use the STEAM classroom from 8-12 Monday, Wednesday, and Thursday. During this time, students will follow the SCOPE curriculum. This program is also available to the public. The Village Childcare center will go in-depth with the following:
            </p>
            <p>
                <strong>Nature and Science:</strong> to comprehend the physical and natural world through observation, description, prediction, and data gathering.
            </p>
            <p>
                <strong>Early Math:</strong> learning about numbers, patterns, sorting, and ordering; to utilize numbers to add, subtract, measure, and graph.
            </p>
            <p>
                <strong>Logic and Reasoning:</strong> practicing sequencing, problem-solving, and critical thinking.
            </p>
            <hr>
            <p>
                Learn more about the Highscope curriculum: <a href="https://highscope.org" target="_blank">here</a>.
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
                We know it can be stressful to find care for your children before and after school care. We offer care with Kalamazoo bus transportation. While your children are with us during this time, they will have the opportunity to relax, do homework, play outside, and play in our S.T.E.A.M room classroom.
            </p>
            <p>
            <strong>Note: </strong>If there is a bus cancellation, we are unable to bus your child&nbsp;to&nbsp;school.
            </p>
        `,
        contentSecondary: `
            <h3>
                Summer Camp + School Breaks
            </h3>
            <p>
                This camp program is for elementary schoolers who are 5-12 years old. We guarantee your children will love spending their summers at the Village Childcare Center. We offer both onsite and offsite field trips. The spaces and activities are designed to be fun, engaging, and educational.
            </p>
            <p>
                No matter the weather, we will be enjoying the outdoors.
            </p>
            <p>
                <strong>Note: </strong>The Village Childcare Center follows the KPS school schedule.
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
                We strongly encourage parents to schedule a tour of the school. This will give you the opportunity to see the classrooms and witness firsthand what your child can experience at The Village Childcare Center.
            </p>
            <p>
                If you have any questions or concerns, or you would like to schedule a tour, please contact us below.
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
                    Westwood Plaza
                </li>
                <li>
                5320 Holiday Terrace, Suite 4
                </li>
                <li>
                    Building A - Lower Level
                </li>
                <li>
                    Kalamazoo, MI 49009
                </li>
            </ul>
            <ul>
                <li>
                    <strong>Local:</strong> (269) 365-0808
                </li>
                <li>
                    <strong>Fax:</strong> (269) 270-3768
                </li>
            </ul>
        `,
    },
    confirm: {
        title: `Thank you`,
        content: `
            <h3>
                Thank you for your interest in The Village Childcare Center!
            </h3>
            <h5>
                We look forward to working with you and your child.
                We'll be in touch soon.
            </h5>
            <img src="${django.staticPrefix + 'img/thanks.png'}" />
        `,
    },
    employment: {
        title: `Employment Information`,
        content: `
            <p>
                The Village Childcare Center is a nature-focused, play-based center inspired by the Reggio Emilia philosophy. We are dedicated to providing the highest level of care to the children in our community. We are looking for hardworking teachers and administrators who take pride in their work and take ownership of their classrooms.
            </p>
            <p>
                A childcare center is only as good as its teaching staff. Our teachers must deliver professional services in a reputable manner. The early childhood years are a very special time in a child's development. Great changes occur in this relatively short period of time as children learn to communicate, increase their intellectual awareness, and make great physical strides.
            </p>
            <p>
                The Village Childcare Center's philosophy is to provide an age-appropriate environment to develop self-esteem, confidence, and a love of learning. By combining the best possible equipment and professionally educated staff in an environment specifically designed for young children, we can provide an outstanding program. Our educational goal is to utilize play and creativity to foster a love of learning. We challenge our students by promoting inquiry and discovery through exploring the world around them, using the environment as a third teacher. This instills a sense of confidence in their ability to master new situations and tasks through reasoning.
            </p>
            <p>
                <strong>Job Description</strong>
            </p>
            <p>
                The following responsibilities are required but not limited to:
            </p>
            <ol>
                <li>
                    Provide complete care for a group of children, including diapering, toilet training, feeding, providing educational opportunities, and serving as a positive role model.
                </li>
                <li>
                    Maintain a sanitary and safe classroom environment through cleaning methods and regular inspection of supplies and facility structure.
                </li>
                <li>
                    Communicate with parents daily regarding each child's progress and daily activities.
                </li>
                <li>
                    Create and implement lesson plans, daily schedules, and cooperative learning plans.
                </li>
                <li>
                    Present a friendly learning environment while maintaining a positive attitude.
                </li>
                <li>
                    Practice and encourage growth and development habits.
                </li>
                <li>
                    Maintain adequate care for all supplies and learning centers.
                </li>
                <li>
                    Ensure that your personnel file, as well as the regulations required to work in a childcare center, are current and documented as required.
                </li>
            </ol>
            <p>
                <strong>Requirements</strong>
            </p>
            <ol>
                <li>
                    Be at least 18 years of age.
                </li>
                <li>
                    Possess a high school diploma or equivalent education.
                </li>
                <li>
                    Be willing to submit to various background checks, including those completed by the Department of Human Services and the Michigan State Police Department.
                </li>
                <li>
                    Be CPR, First Aid, and Blood Borne Pathogen certified or willing to obtain certification upon hire.
                </li>
                <li>
                    Complete a Tuberculosis test and physical and provide a physician's documentation of both.
                </li>
                <li>
                    Complete 12 hours of pre-approved continued education per calendar year, with 3 hours of these being face-to-face.
                </li>
            </ol>
            <p>
                <strong>Benefits</strong>
            </p>
            <ol>
                <li>
                    Employee discount.
                </li>
                <li>
                    Paid time off.
                </li>
            </ol>
            <p>
            <strong>How to Apply</strong>
            </p>
            <p>
            Please send your completed <a href="${django.staticPrefix + 'img/VCC-App.pdf'}">application</a>, along with your resume and cover letter, to <a href="mailto:director@thevillageccc.com">our director</a>.
            </p>
            <p>
                <i>*Note: Please do NOT apply for a lead teacher position if you do not meet all state qualifications to be approved as a lead teacher.</i>
            </p>
        `,
    },
};

const hasSecondaryContent = [
    'home',
    'classrooms',
    'school_age',
    'contact',
    'steam',
]


/**
 * Show the secondary content for the page and update the title and content if set.
 * @param {bool} updateContent
 * @returns {() => void}
 */
function showSecondaryContent(updateContent) {
    return () => {
        const $handleFieldWrapper = $('.field-handle');
        const $handleSelect = $('#id_handle');
        const handle = $handleSelect.val();
        if (!updateContent && handle) {
            $handleFieldWrapper.hide();
        }
        const $title = $('#id_title');
        const mceContent = tinymce.get("id_content");
        const $contentSecondary = $('.field-content_secondary');
        const mceContentSecondary = tinymce.get("id_content_secondary");

        if (updateContent) {
            console.log('updating content');
            console.log(pageDefaults[handle].content);
            mceContent.setContent(pageDefaults[handle].content);
        }

        if (pageDefaults[handle] && pageDefaults[handle].title) {
            $title.val(pageDefaults[handle].title);
        }

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


const hasAccordionContent = [
    'classrooms',
    'philosophy',
]

/**
 * Show the accordion content for the page and update the title and content if set.
 * @param {bool} updateContent
 * @returns {() => void}
 */
function showAccordion(updateContent) {
    return () => {
        const $handleFieldWrapper = $('.field-handle');
        const $handleSelect = $('#id_handle');
        const handle = $handleSelect.val();
        if (!updateContent && handle) {
            $handleFieldWrapper.hide();
        }
        const $title = $('#id_title');
        const mceContent = tinymce.get("id_content");
        const $accordion = $('.field-accordion');
        const mceAccordion = tinymce.get("id_accordion");

        if (updateContent) {
            console.log('updating content');
            console.log(pageDefaults[handle].content);
            mceContent.setContent(pageDefaults[handle].content);
        }

        if (pageDefaults[handle] && pageDefaults[handle].title) {
            $title.val(pageDefaults[handle].title);
        }

        if (hasAccordionContent.includes(handle) && $accordion.length) {
            $accordion.show();
            if (updateContent) {
                mceAccordion.setContent(pageDefaults[handle].accordion);
            }
        } else {
            $accordion.hide();
        }
    }
}

$(showAccordion(false));
$('#id_handle').on('change', showAccordion(true));

const hasSecondaryAccordion = [
    'classrooms',
]

/**
 * Show the secondary accordion content for the page and update the title and content if set.
 * @param {bool} updateContent
 * @returns {() => void}
 */
function showSecondaryAccordion(updateContent) {
    return () => {
        const $handleFieldWrapper = $('.field-handle');
        const $handleSelect = $('#id_handle');
        const handle = $handleSelect.val();
        if (!updateContent && handle) {
            $handleFieldWrapper.hide();
        }
        const $title = $('#id_title');
        const mceContent = tinymce.get("id_content");
        const $accordionSecondary = $('.field-accordion_secondary');
        const mceAccordionSecondary = tinymce.get("id_accordion_secondary");

        if (updateContent) {
            console.log('updating content');
            console.log(pageDefaults[handle].content);
            mceContent.setContent(pageDefaults[handle].content);
        }

        if (pageDefaults[handle] && pageDefaults[handle].title) {
            $title.val(pageDefaults[handle].title);
        }

        if (hasSecondaryAccordion.includes(handle) && $accordionSecondary.length) {
            $accordionSecondary.show();
            if (updateContent) {
                mceAccordionSecondary.setContent(pageDefaults[handle].accordionSecondary);
            }
        } else {
            $accordionSecondary.hide();
        }
    }
}

$(showSecondaryAccordion(false));
$('#id_handle').on('change', showSecondaryAccordion(true));
