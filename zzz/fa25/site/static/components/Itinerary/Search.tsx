

interface SearchProps {
    data: object;
    defaultText: string;
    callback: (searching: boolean, data: object) => void;
}

class Search extends React.Component<SearchProps> {
    inputRef: any;
    constructor(props) {
        super(props);
        this.inputRef = React.createRef();
    }

    onKeyUp(event) {

        const searchQuery: string = this.inputRef.current.value;
        if (searchQuery) {
            const results = this.search(searchQuery);
            this.props.callback(true, results);
        } else {
            this.props.callback(false, {});
        }


    }

    checkForValue(json, query) {
        for (const key in json) {
            if (key === "links") {
                for (const linkTitle in json[key]) {
                    if (linkTitle.toLowerCase().includes(query.toLowerCase())) {
                        return true;
                    }
                }
            } else if (typeof (json[key]) === "object") {
                return this.checkForValue(json[key], query);
            } else if (typeof json[key] === "number") {
                if (json[key] === query) {
                    return true;
                }
            } else {
                if (json[key].toLowerCase().includes(query.toLowerCase())) {
                    return true;
                }
            }
        }
        return false;
    }

    search(query: string): object {
        const { data } = this.props;
        let new_data = {};

        console.log("running");
        for (const date in data) {
            if (data[date].length > 0) {
                if (date.includes(query)) {
                    new_data[date] = data[date];
                } else {
                    for (let i = 0; i < data[date].length; i++) {
                        if (this.checkForValue(data[date][i], query)) {
                            if (!(date in new_data)) {
                                new_data[date] = [];
                            }
                            new_data[date].push(data[date][i]);
                        }
                    }
                }
            }
        }
        return new_data;
    }

    render() {
        return <div className="col search-col">
            <input ref={this.inputRef} className="search" type="text" placeholder={this.props.defaultText} onKeyUp={this.onKeyUp.bind(this)} />
        </div>;
    }
}