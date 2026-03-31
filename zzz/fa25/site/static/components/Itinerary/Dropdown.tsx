interface DropdownProps {
    name: string;
    options: object;
    callback: (type: string) => void;
    singleSelect?: boolean;
    startKey?: string;
    startKeys?: any;
}

interface DropdownState {
    clicked: boolean;
}

class Dropdown extends React.Component<DropdownProps, DropdownState> {
    buttonRefs: object;
    constructor(props) {
        super(props);
        this.buttonRefs = {};
        this.state = { clicked: false } ;
        if (this.props.singleSelect) {
            for (const option in this.props.options) {
                this.buttonRefs[option] = React.createRef();
            }
        }
    }

    handleSingleSelect(selected: string) {
        for (const option in this.props.options) {
            if (option != selected) {
                this.buttonRefs[option].current.deselect();
            }
        }
        this.props.callback(selected);
    }


    render() {
        if (this.state.clicked) {
            let optionButtons = [];
            for (const option in this.props.options) {
                if (this.props.singleSelect) {
                    optionButtons.push(<DropdownButton singleSelect={true} startSelect={this.props.startKey === (option)} key={option} ref={this.buttonRefs[option]} label={this.props.options[option]} callback={() => { this.handleSingleSelect(option); }}>
                        {this.props.options[option]}</DropdownButton>);
                }
                else {
                    optionButtons.push(<DropdownButton startSelect={this.props.startKeys.has(option)} ref={this.buttonRefs[option]} key={option} label={this.props.options[option]} callback={() => { this.props.callback(option); }}>
                        {this.props.options[option]}</DropdownButton>);
                }
            }
            

            return <div id="type-button">
                <button id="type-button" className="filter-feature-button btn" onClick={() => this.setState({ clicked: false })}>
                    {this.props.name}
                    <img src="/static/components/Itinerary/arrow-up.png" style={{ marginLeft: ".5rem", maxWidth: ".75rem" }}></img>
                    </button>
                <div className={"dropdown-container"}>{optionButtons}</div>
            </div>

        } else {
            return <button id="type-button" className="filter-feature-button btn" onClick={() => this.setState({ clicked: true })}>
                {this.props.name}<img src="/static/components/Itinerary/arrow-down.png" style={{ marginLeft: ".5rem", maxWidth: ".75rem" }}></img></button>;
        }

    }
}