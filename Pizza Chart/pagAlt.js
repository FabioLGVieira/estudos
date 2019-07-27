function createGraph(){
    const valorJan = document.getElementById("inputJan");
    const valorFev = document.getElementById("inputFev");
    const valorMar = document.getElementById("inputMar");
    const valorAbr = document.getElementById("inputAbr");
    const valorMai = document.getElementById("inputMai");
    const valorJun = document.getElementById("inputJun");
    const valorJul = document.getElementById("inputJul");
    document.getElementById("barraJan").style.height = valorJan.value;
    document.getElementById("barraFev").style.height = valorFev.value;
    document.getElementById("barraMar").style.height = valorMar.value;
    document.getElementById("barraAbr").style.height = valorAbr.value;
    document.getElementById("barraMai").style.height = valorMai.value;
    document.getElementById("barraJun").style.height = valorJun.value;
    document.getElementById("barraJul").style.height = valorJul.value;
}