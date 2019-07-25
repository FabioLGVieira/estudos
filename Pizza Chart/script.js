function changeStyle(sheet){
    document.getElementById('style-page').setAttribute('href', sheet);
}

function run() {
    const pAtum = [13, 23, 20, 22, 17, 21, 15];
    const pMarguerita = [19, 17, 14, 21, 22, 19, 28];
    const pPeperoni = [24, 28, 25, 17, 19, 21, 19];
    const pQueijos = [27, 20, 29, 25, 23, 26, 22];
    const pizzasVendidas = [0, 0, 0, 0, 0, 0, 0];
    const appVendidas = [32, 28, 35, 47, 43, 29, 34];
    const telVendidas = [0, 0, 0, 0, 0, 0, 0];
    for (let i = 0; i < pizzasVendidas.length; i++) {
        pizzasVendidas[i] = pAtum[i] + pMarguerita[i] + pPeperoni[i] + pQueijos[i];
        telVendidas[i] = pizzasVendidas[i] - appVendidas[i];
    }

    const ctx = document.getElementById('salesChart').getContext('2d');
    const barChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul'],
            datasets: [{
                label: 'Pizza de Atum',
                data: pAtum,
                backgroundColor:
                    'rgba(204, 136, 0, 0.3)',
                borderWidth: 2
            }, {
                type: 'bar',
                label: 'Pizza Marguerita',
                data: pMarguerita,
                backgroundColor:
                    'rgba(83, 198, 140, 0.3)',
                borderWidth: 2
            }, {
                type: 'bar',
                label: 'Pizza de Peperoni',
                data: pPeperoni,
                backgroundColor:
                    'rgba(255, 50, 50, 0.3)',
                borderWidth: 2
            }, {
                type: 'bar',
                label: 'Pizza 4 Queijos',
                data: pQueijos,
                backgroundColor:
                    'rgba(255, 206, 86, 0.3)',
                borderWidth: 2
            }, {
                type: 'line',
                label: 'Qtde. de Pizzas vendidas',
                data: pizzasVendidas,
                lineTension: 0,
                fill: false,
                borderColor: 'rgba(141, 177, 146, 0.7)',
                borderWidth: 5
            }, {
                type: 'line',
                label: 'Pedidos pelo aplicativo',
                data: appVendidas,
                fill: false,
                borderColor: 'rgba(56, 74, 92, 0.7)',
                borderWidth: 5
            }, {
                type: 'line',
                label: 'Pedidos pelo telefone',
                data: telVendidas,
                fill: false,
                borderColor: 'rgba(98, 125, 189, 0.7)',
                borderWidth: 5
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });

}