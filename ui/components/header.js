export default class Header {
    constructor(title) {
        this.title = title
    }

    render() {
        return `<h2 class="header">${this.title}</h2>`        
    }

}