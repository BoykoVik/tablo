getDate();

function getDate(){
    var date = new Date();
    var year = date.getFullYear()
    var day = date.getDate()
    var month = date.getMonth() + 1;
    var hours = date.getHours();
    var minutes = date.getMinutes();
    switch(month) {
        case 1:
            monthstr = 'января';
            break;
        case 2:
            monthstr = 'февраля';
            break;
        case 3:
            monthstr = 'марта';
            break;
        case 4:
            monthstr = 'апреля';
            break;
        case 5:
            monthstr = 'мая';
            break;
        case 6:
            monthstr = 'июня';
            break;
        case 7:
            monthstr = 'июля';
            break;
        case 8:
            monthstr = 'августа';
            break;
        case 9:
            monthstr = 'сентября';
            break;
        case 10:
            monthstr = 'октября';
            break;
        case 11:
            monthstr = 'ноября';
            break;
        case 12:
            monthstr = 'декабря';
            break;
    }
    document.getElementsByClassName('year')[0].innerHTML = year;
    document.getElementsByClassName('date')[0].innerHTML = day +' '+ monthstr;
    document.getElementsByClassName('time')[0].innerHTML = hours +':'+ minutes;
}
setTimeout(getDate, 10);