// base.html
// 현재 페이지에 해당하는 네비게이션 링크 활성화
document.addEventListener('DOMContentLoaded', function() {
    const currentLocation = window.location.pathname;
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentLocation) {
            link.classList.add('active');
        }
    });
    
    // main 페이지에서만 스크롤 시 네비게이션 바 스타일 변경 적용
    const body = document.body;
    if (body.classList.contains('main-page')) {
        // 스크롤 시 네비게이션 바 스타일 변경
        window.addEventListener('scroll', function() {
            const navbar = document.querySelector('.navbar');
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
        
        // 네비게이션 로고 업데이트 함수 (main 페이지에서만)
        const logo = document.getElementById('navbar-logo');
        if (logo) {
            const whiteLogo = "/static/assets/img/encle_logo_white.png";
            const blackLogo = "/static/assets/img/encle_logo_black.png";
            
            function updateLogo() {
                if (window.scrollY > 50) {
                    logo.src = blackLogo;
                } else {
                    logo.src = whiteLogo;
                }
            }
            window.addEventListener('scroll', updateLogo);
        }
    } else {
        // main 페이지가 아닌 다른 페이지에서는 검은색 로고와 글씨 적용
        const navbar = document.querySelector('.navbar');
        const logo = document.getElementById('navbar-logo');
        
        if (navbar) {
            navbar.classList.add('scrolled');
        }
        
        if (logo) {
            logo.src = "/static/assets/img/encle_logo_black.png";
        }
    }
    
    // 숫자 카운트업 애니메이션
    function animateCountUp(element, targetNumber, duration = 2000) {
        let startNumber = 0;
        const increment = targetNumber / (duration / 16); // 60fps
        let currentNumber = 0;
        
        element.classList.add('count-up-animation');
        
        const timer = setInterval(() => {
            currentNumber += increment;
            if (currentNumber >= targetNumber) {
                currentNumber = targetNumber;
                clearInterval(timer);
            }
            
            // 숫자에 따라 표시 형식 조정
            const roundedNumber = Math.floor(currentNumber);
            if (targetNumber === 98) {
                element.textContent = roundedNumber + '%';
            } else {
                element.textContent = roundedNumber + '+';
            }
        }, 16);
    }
    
    // Intersection Observer로 요소가 화면에 나타날 때 애니메이션 시작
    const observerOptions = {
        threshold: 0.5,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const statNumbers = entry.target.querySelectorAll('.stat-number');
                statNumbers.forEach(stat => {
                    // 각 통계의 최종 값 정의
                    const finalValues = {
                        '완료 프로젝트': 50,
                        '고객사': 30,
                        '고객 만족도': 98
                    };
                    
                    // 라벨을 찾아서 해당하는 최종 값 가져오기
                    const statItem = stat.closest('.stat-item');
                    const label = statItem.querySelector('.stat-label');
                    const labelText = label.textContent.trim();
                    
                    if (finalValues[labelText]) {
                        animateCountUp(stat, finalValues[labelText]);
                    }
                });
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // 통계 섹션 관찰 시작
    const statsSection = document.querySelector('.stats-container');
    if (statsSection) {
        observer.observe(statsSection);
    }
});

// navigation.html
// 드롭다운 메뉴 호버 기능
document.addEventListener('DOMContentLoaded', function() {
    const dropdown = document.getElementById('referenceDropdown');
    if (dropdown) {
        const dropdownMenu = dropdown.querySelector('.dropdown-menu');
        let timeoutId;

        // 마우스가 드롭다운 영역에 들어올 때
        dropdown.addEventListener('mouseenter', function() {
            clearTimeout(timeoutId);
            dropdownMenu.style.display = 'block';
            dropdownMenu.style.opacity = '1';
            dropdownMenu.style.transform = 'translateY(0)';
        });

        // 마우스가 드롭다운 영역을 벗어날 때
        dropdown.addEventListener('mouseleave', function() {
            timeoutId = setTimeout(function() {
                dropdownMenu.style.display = 'none';
                dropdownMenu.style.opacity = '0';
                dropdownMenu.style.transform = 'translateY(-10px)';
            }, 300); // 300ms 지연
        });

        // 드롭다운 메뉴에 마우스가 들어올 때 타이머 취소
        dropdownMenu.addEventListener('mouseenter', function() {
            clearTimeout(timeoutId);
        });

        // 드롭다운 메뉴에서 마우스가 벗어날 때
        dropdownMenu.addEventListener('mouseleave', function() {
            timeoutId = setTimeout(function() {
                dropdownMenu.style.display = 'none';
                dropdownMenu.style.opacity = '0';
                dropdownMenu.style.transform = 'translateY(-10px)';
            }, 300); // 300ms 지연
        });
    }
});

// main/index.html
let currentSlide = 1;
const totalSlides = 3;

function changeServiceSlide(direction) {
    const slides = document.querySelectorAll('.service-slide');
    const indicators = document.querySelectorAll('.indicator');
    
    // 현재 슬라이드 숨기기
    slides.forEach(slide => slide.classList.remove('active'));
    indicators.forEach(indicator => indicator.classList.remove('active'));
    
    // 새 슬라이드 계산
    currentSlide += direction;
    if (currentSlide > totalSlides) currentSlide = 1;
    if (currentSlide < 1) currentSlide = totalSlides;
    
    // 새 슬라이드 보이기
    document.querySelector(`[data-slide="${currentSlide}"]`).classList.add('active');
    document.querySelector(`.indicator[data-slide="${currentSlide}"]`).classList.add('active');
}

// 인디케이터 클릭 이벤트
document.addEventListener('DOMContentLoaded', function() {
    const indicators = document.querySelectorAll('.indicator');
    indicators.forEach(indicator => {
        indicator.addEventListener('click', function() {
            const targetSlide = parseInt(this.getAttribute('data-slide'));
            const slides = document.querySelectorAll('.service-slide');
            const allIndicators = document.querySelectorAll('.indicator');
            
            // 모든 슬라이드와 인디케이터 비활성화
            slides.forEach(slide => slide.classList.remove('active'));
            allIndicators.forEach(ind => ind.classList.remove('active'));
            
            // 선택된 슬라이드와 인디케이터 활성화
            document.querySelector(`[data-slide="${targetSlide}"]`).classList.add('active');
            this.classList.add('active');
            currentSlide = targetSlide;
        });
    });
});