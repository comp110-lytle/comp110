interface EventSectionProps {
    event: EventObject;
}

class EventSection extends React.Component<EventSectionProps> {
    constructor(props) {
        super(props);
    }

    parseN(n) {
        return n < 10 ? `0${n}` : `${n}`;
    }

    render() {

        let links = [];
        for (const link in this.props.event.links) {
            const url = this.props.event.links[link]
            if (url.includes("zoom") || url.includes("course.care") || url.includes("youtu") ||  url.includes("grades") || url.includes("bit")) {
                // links.push(<li className="link" onClick={() => window.open(url, "_blank")}><a>{link}</a> </li>);
                links.push(<li className="link"><a href={url} target="_blank">{link}</a> </li>);
            }
            else {
                // links.push(<li className="link" onClick={() => window.open(url, "_self", 'noopener,noreferrer')}><a>{link}</a> </li>);
                links.push(<li className="link"><a href={url} target="_self">{link}</a> </li>);
            }

        }

        let linkSection = (<ul className="links">{links}
        </ul>);

        if (links.length > 0) {
            return <div className="plan Reviews" >
                <span className="kind" > {this.props.event.kind}{this.parseN(this.props.event.n)} </span> -
                < span className="title" > {this.props.event.title} </span>{linkSection}</div >;
        } else {
            return <div className="plan Reviews" >
                <span className="kind" > {this.props.event.kind}{this.parseN(this.props.event.n)} </span> -
                < span className="title" > {this.props.event.title} </span></div >;
        }

    }
}