

interface PillButtonsProps {
    name: string;
    options: object;
    callback: (type: string) => void;
    singleSelect?: boolean;
    startKey?: string;
    startKeys?: any;
}

class PillButtons extends React.Component<PillButtonsProps> {
    buttonRefs: object;
    constructor(props) {
        super(props);
        this.buttonRefs = {};
        if (this.props.singleSelect) {
            for (const option in this.props.options) {
                this.buttonRefs[option] = React.createRef();
                console.log(this.buttonRefs)
            }
        }
    }

    componentDidMount() {
        if (this.props.singleSelect) {
            // console.log(this)
            // console.log(this.buttonRefs)
            // console.log(this.props.startKey)
            // console.log(this.buttonRefs[this.props.startKey])
            // console.log(this.buttonRefs[this.props.startKey].current)
            this.buttonRefs[this.props.startKey].current.select();
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
        let optionButtons = [];
        for (const option in this.props.options) {
            if (this.props.singleSelect) {
                optionButtons.push(<PillButton singleSelect={true} ref={this.buttonRefs[option]} label={this.props.options[option]} callback={() => { this.handleSingleSelect(option); }} />);
            } else {
                optionButtons.push(<PillButton startSelect={this.props.startKeys.has(option)} label={this.props.options[option]} callback={() => { this.props.callback(option); }} />);
            }
        }
        return <div>
            <p className="pill-button-header">{this.props.name}</p>
            {optionButtons}
        </div>;
    }
}