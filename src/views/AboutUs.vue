<template>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Responsive Our Team Section</title>
        <link
          rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
        />
        <link
          href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;600&display=swap"
          rel="stylesheet"
        />
        <link rel="stylesheet" href="style.css" />
      </head>
      <body>
        <section>
            <div class="row">
                <h1>Our Team</h1>
            </div>
            <div class="row">
                <!-- Page -->
                <div class="column">
                    <div class="card">
                        <div class="img-container">
                            <img src="@/assets/test.jpeg" alt="test"/>
                        </div>
                        <h3>Page</h3>
                        <p>B.S. Quantitative Sciences and Informatics</p>
                        <div class="icons">
                            <a href="https://www.linkedin.com/in/page-nellis?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app" target="_blank">
                                <i class="fab fa-linkedin"></i>
                            </a>
                            <a href="https://github.com/pnellis" target="_blank">
                                <i class="fab fa-github"></i>
                            </a>
                            <a href="mailto:page.nellis@emory.edu" target="_blank">
                                <i class="fas fa-envelope"></i>
                            </a>
                        </div>
                    </div>
                </div>
                 <!-- Cristina -->
                 <div class="column">
                    <div class="card">
                        <div class="img-container">
                            <img src="@/assets/test.jpeg" alt="test"/>
                        </div>
                        <h3>Cristina</h3>
                        <p>B.S. Computer Science</p>
                        <div class="icons">
                            <a href="https://www.linkedin.com/in/cristinaram?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app" target="_blank">
                                <i class="fab fa-linkedin"></i>
                            </a>
                            <a href="https://github.com/cristinar07" target="_blank">
                                <i class="fab fa-github"></i>
                            </a>
                            <a href="mailto:cristina.ramirez@emory.edu" target="_blank">
                                <i class="fas fa-envelope"></i>
                            </a>
                        </div>
                    </div>
                </div>   
                <!-- Carol -->
                <div class="column">
                    <div class="card">
                        <div class="img-container">
                            <img src="@/assets/test.jpeg" alt="test"/>
                        </div>
                        <h3>Carol (Zijing) Zhou</h3>
                        <p>B.S. Biology and Quantitative Science (Informatics) </p>
                        <div class="icons">
                            <a href="https://www.linkedin.com/in/zijing-zhou-b674601b6/" target="_blank">
                                <i class="fab fa-linkedin"></i>
                            </a>
                            <a href="https://github.com/zz-carol" target="_blank">
                                <i class="fab fa-github"></i>
                            </a>
                            <a href="mailto:carol.zhou@emory.edu" target="_blank">
                                <i class="fas fa-envelope"></i>
                            </a>
                        </div>
                    </div>
                </div>                            
                <!-- audrey -->
                <div class="column">
                    <div class="card">
                        <div class="img-container">
                            <img src="@/assets/audrey.jpg" alt="test"/>
                        </div>
                        <h3>Audrey Poon</h3>
                        <p>B.S. Computer Science</p>
                        <div class="icons">
                            <a href="https://www.linkedin.com/in/audrey-p-6b957a1b2/" target="_blank">
                                <i class="fab fa-linkedin"></i>
                            </a>
                            <a href="https://github.com/audreyp00n" target="_blank">
                                <i class="fab fa-github"></i>
                            </a>
                            <a href="mailto:apoon5@emory.edu" target="_blank">
                                <i class="fas fa-envelope"></i>
                            </a>
                        </div>
                    </div>
                </div>
          
                <!-- Katie -->
                <div class="column">
                    <div class="card">
                        <div class="img-container">
                            <img src="@/assets/test.jpeg" alt="test"/>
                        </div>
                        <h3>Katie (Mingchen) Shao</h3>
                        <p>B.S. Applied Math & Statistics and Computer Science</p>
                        <div class="icons">
                            <a href="https://www.linkedin.com/in/mingchen-shao-30309a246/" target="_blank">
                                <i class="fab fa-linkedin"></i>
                            </a>
                            <a href="https://github.com/KatieShao" target="_blank">
                                <i class="fab fa-github"></i>
                            </a>
                            <a href="mailto:katie.shao@emory.edu" target="_blank">
                                <i class="fas fa-envelope"></i>
                            </a>
                        </div>
                    </div>
                </div>
                <!-- Ralph -->
   
            </div>
        </section>


    </body>
</template>

<style scoped>
* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    font-family: "Poppins", sans-serif;
}
body {
    background-color: #fcb4c6;
}
.row {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    padding: 1em 1em;
    text-align: center;
}
.column {
    flex: 0 0 calc(33.33% - 20px); /* Divide container into 3 columns  */
    max-width: calc(33.33% - 20px);
    padding: 1em;
}

h1 {
    width: 100%;
    text-align: center;
    font-size: 3.5em;
    color: #6bd4d3;
}
.card {
    box-shadow: 0 0 2.4em #dedbdc;;
    padding: 3.5em 1em;
    border-radius: 0.6em;
    color: #1f003b;
    cursor: pointer;
    transition: 0.3s;
    background-color: #ffebf0;
}
.card .img-container {
    width: 8em;
    height: 8em;
    background-color: #f792ac;
    padding: 0.5em;
    border-radius: 50%;
    margin: 0 auto 2em auto;
}
.card img {
    width: 100%;
    border-radius: 50%;
}
.card h3 {
    font-weight: 500;
}
.card p {
    font-weight: 300;
    text-transform: uppercase;
    margin: 0.5em 0 2em 0;
    letter-spacing: 2px;
}
.icons {
    width: 50%;
    min-width: 180px;
    margin: auto;
    display: flex;
    justify-content: space-between;
}
.card a {
    text-decoration: none;
    color: inherit;
    font-size: 1.4em;
}
.card:hover {
    background: linear-gradient(#6bd4d3, #c9f0f0);
    color: #ffffff;
}
.card:hover .img-container {
    transform: scale(1.15);
}
/* fit different devices */
@media screen and (min-width: 768px) {
    section {
        padding: 1em 7em;
    }
    .column {
        flex: 0 0 calc(33.33% - 2em);
        max-width: calc(33.33% - 2em);
    }
}
</style>