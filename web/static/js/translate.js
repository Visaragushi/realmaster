function googleTranslateElementInit() {
    new google.translate.TranslateElement({
            pageLanguage: 'en', 
            includedLanguages: 'en,sq,mk,sr,fr,de,tr', 
        },
        'google_translate_element'
    );
}

window.onload = function() {
    var languageSelector = document.querySelector('.goog-te-combo');
    var parentElement = languageSelector.parentElement;
    parentElement.style.display = 'block';

    // Define flag icon classes for each language
    var languages = {
        'sq': 'flag-icon-al',
        'en': 'flag-icon-us',
        'mk': 'flag-icon-mk',
        'sr': 'flag-icon-rs',
        'fr': 'flag-icon-fr',
        'de': 'flag-icon-de'
    };

    // Loop through language options and create flag icon elements
    var languageOptions = languageSelector.options;
    for (var i = 0; i < languageOptions.length; i++) {
        var languageCode = languageOptions[i].value;
        if (languages[languageCode]) {
            var flagIcon = document.createElement('span');
            flagIcon.setAttribute('class', 'flag-icon ' + languages[languageCode] + ' goog-te-menu-value');
            flagIcon.setAttribute('style', 'cursor: pointer; margin-right: 5px;');
            flagIcon.setAttribute('data-lang', languageCode);
            flagIcon.addEventListener('click', function() {
                languageSelector.value = this.getAttribute('data-lang');
                languageSelector.dispatchEvent(new Event('change'));
            });

            parentElement.appendChild(flagIcon);
        }
    }

    // delete iframe
    var iframe = document.querySelector('iframe');
    if (iframe) {
        iframe.remove();
    }
};