import Header from "./header.js";
import Host from "./host.js";

export default class App{
    constructor(hosts){
        this.appElement = null
        
        this.hosts = []
        this.header = new Header('pinginfoview.py')
        hosts.forEach(host => {
            this.hosts.push(new Host(host));
        })
    }

    init() {
        this.appElement = document.querySelector('.app')
        setInterval(() => {
            this.fastRender()
        }, 5000)
    }

    renderInnerHTML() {
        let result = this.header.render()
        this.hosts.forEach(host => {
            result += host.render()
        })
        return `${result}`
    }

    fastRender() {
        this.hosts.forEach(host => {
            host.renderViaAttr()
        })
    }

    render() {
        console.log('render')
        this.appElement.innerHTML = this.renderInnerHTML()
    }

}