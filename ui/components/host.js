export default class Host{
    constructor(host) {
        this.host = host
        this.imgPath = null
        this.imgPath = '/images/' + btoa(this.host) + '.png';
        this.class = `img-${this.getRandomInt(1, 10000)}`
    }

    init() {
        console.log(this.imgPath)
    }

    render() {
        return this.renderInnerHTML()
    }

    renderInnerHTML() {
        let time = "?" + new Date().getTime()
        return `<img class="host-img ${this.class}" src="${this.imgPath}${time}">`
    }

    renderViaAttr() {
        if (this.element == null)
            this.element = document.querySelector('.'+this.class)
        let time = "?" + new Date().getTime()
        this.element.setAttribute('src', `${this.imgPath}${time}`)
    }

    getRandomInt(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }
}