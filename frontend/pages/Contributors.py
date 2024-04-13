import streamlit as st

st.markdown("""
<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
</head>



<style>
.st-ag-card {
    margin: 20px 0 20px 20px;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    overflow: auto;
    background: linear-gradient(315deg, #4f2991 3%, #7dc4ff 38%, #36cfcc 68%, #a92ed3 98%);
    animation: gradient 15s ease infinite;
    background-size: 400% 400%;
    background-attachment: fixed;
    border-radius: 10px;
    box-shadow: 0 19px 19px rgba(0, 0, 0, 0.3);
    width: 540px;
    height: auto;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;  /* Align items to the right */
    padding: 1rem;
}

.st-ag-card-img {
    width: 100px;
    border-radius: 150px;
    margin-right: 1rem;
}

.st-ag-card-title {
    font-size: 1.25rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.st-ag-card-text {
    font-size: 1rem;
    line-height: 1.5;
    margin-bottom: 0.5rem;
    color: #000000;
}

.st-ag-card-timestamp {
    font-size: 0.75rem;
    color: #000000;
    margin-bottom: 0;
}

.st-icon-link {
    margin-left: 50px;  /* Add margin between icons */
    text-decoration: none;  /* Remove underline */
    font-size: 25px;
}

</style>


<div class="st-ag-card">
    <img src="https://media.licdn.com/dms/image/D5603AQELf7x7w_UX-Q/profile-displayphoto-shrink_400_400/0/1692427240463?e=1717632000&v=beta&t=X8yqsmO9FZwN5VCMJ81GkIfpVIqRUoGOY5psdjS9nzg" class="st-ag-card-img" alt="...">
    <div class="st-ag-card-body">
        <h5 class="st-ag-card-title">MOTAPOTULA MADHAVAN</h5>
        <p class="st-ag-card-text">Computer Science and Engineering (Data Science)</p>
        <p class="st-ag-card-timestamp"><small class="text-body-secondary">RGMCET</small></p>
        <div>
            <a href="https://www.linkedin.com/in/motapotula-madhavan-064b5616b/" class="st-icon-link">
                <i class="fab fa-linkedin"></i> <!-- LinkedIn icon -->
            </a>
            <a href="https://github.com/Madhavan-github2" class="st-icon-link" style="color: black;">
                <i class="fab fa-github"></i> <!-- GitHub icon -->
            </a>
            <a href="mailto:madhavanrockzzz31@gmail.com" class="st-icon-link">
                <i class="fas fa-envelope" style="color: red;"></i> <!-- Mail icon -->
            </a>
        </div>
    </div>
</div>


<div class="st-ag-card">
    <img src="https://media.licdn.com/dms/image/D5603AQFZN9mE8a-sTw/profile-displayphoto-shrink_400_400/0/1696802105434?e=1717632000&v=beta&t=dQEnB_k7d4jMFxFHByM0lmWMG9TlOZbeWKRuIrs8c78" class="st-ag-card-img" alt="...">
    <div class="st-ag-card-body">
        <h5 class="st-ag-card-title">MAHESH JAVINIKI</h5>
        <p class="st-ag-card-text">Computer Science and Engineering (Data Science)</p>
        <p class="st-ag-card-timestamp"><small class="text-body-secondary">RGMCET</small></p>
        <div class="iconsdis">
            <a href="https://www.linkedin.com/in/mahesh-javiniki-11060a1ba/" class="st-icon-link">
                <i class="fab fa-linkedin"></i> <!-- LinkedIn icon -->
            </a>
            <a href="https://github.com/javiniki-mahesh" class="st-icon-link" style="color: black;">
                <i class="fab fa-github"></i> <!-- GitHub icon -->
            </a>
            <a href="mailto:maheshjaviniki@gmail.com" class="st-icon-link">
                <i class="fas fa-envelope" style="color: red;"></i> <!-- Mail icon -->
            </a>
        </div>
    </div>
</div>


<div class="st-ag-card">
    <img src="https://media.licdn.com/dms/image/D5603AQFOzqzQ3zV8kQ/profile-displayphoto-shrink_400_400/0/1711956916173?e=1717632000&v=beta&t=rRitRi56BJS4X8MTMLciAQyGgbssqUPfQPQ5TtKoqXg" class="st-ag-card-img" alt="...">
    <div class="st-ag-card-body">
        <h5 class="st-ag-card-title">B.S. ROHITH KUMAR</h5>
        <p class="st-ag-card-text">Computer Science and Engineering (Data Science)</p>
        <p class="st-ag-card-timestamp"><small class="text-body-secondary">RGMCET</small></p>
        <div class="iconsdis">
            <a href="https://www.linkedin.com/in/rohitkumar2106/" class="st-icon-link">
                <i class="fab fa-linkedin"></i> <!-- LinkedIn icon -->
            </a>
            <a href="https://github.com/Rohithkumar77" class="st-icon-link" style="color: black;">
                <i class="fab fa-github"></i> <!-- GitHub icon -->
            </a>
            <a href="mailto:sunkesularohithkumar77@gmail.com" class="st-icon-link">
                <i class="fas fa-envelope" style="color: red;"></i> <!-- Mail icon -->
            </a>
        </div>
    </div>
</div>

""", unsafe_allow_html=True)
