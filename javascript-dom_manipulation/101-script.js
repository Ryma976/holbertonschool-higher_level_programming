document.addEventListener('DOMContentLoaded', function () {
  const btnTranslate = document.querySelector('#btn_translate');
  btnTranslate.addEventListener('click', function () {
    const lang = document.querySelector('#language_code').value;
    if (lang) {
      fetch(`https://hellosalut.stefanbohacek.com/?lang=${lang}`)
        .then((response) => response.json())
        .then((data) => {
          document.querySelector('#hello').textContent = data.hello;
        });
    }
  });
});
