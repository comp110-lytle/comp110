interface DropdownButtonProps {
    label: string;
    callback: () => void;
    startSelect?: boolean;
    singleSelect?: boolean;
}

interface DropdownButtonState {
    clicked: boolean;
}

class DropdownButton extends React.Component<DropdownButtonProps, DropdownButtonState> {
    constructor(props) {
        super(props);
        if (this.props.startSelect) {
            this.state = { clicked: true };
        } else {
            this.state = { clicked: false };
        }
    }

    deselect() {
        this.setState({ clicked: false });
    }
    select() {
        this.setState({ clicked: true });
    }

    handleClick() {
        if (this.props.singleSelect && this.state.clicked) {
            return;
        } else {
            this.setState({ clicked: !this.state.clicked });
            this.props.callback();
        }
    }

    render() {
        if (this.state.clicked) {
            return <button id="type-button" className="btn dropdown-button-off" onClick={this.handleClick.bind(this)}>
                {this.props.label}
            </button>;
        } else {
            return <button id="type-button" className="btn dropdown-button-on" onClick={this.handleClick.bind(this)}>
                {this.props.label}
            </button>;
        }

    }
}