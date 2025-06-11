
interface DatesProps {
    time: "past" | "future" | "all" | "filter";
    dates: object;
    reverse?: boolean;
    type: Set<"LS" | "RD" | "EX" | "PJ" | "RV" | "QZ" | "WD" | "FN" | undefined>;
}

class Dates extends React.Component<DatesProps> {
    constructor(props) {
        super(props);
    }

    dateContainType(date: string) {
        if (!this.props.type.size || this.props.type === undefined) {
            return true;
        }
        for (let i = 0; i < this.props.dates[date].length; i++) {
            if (this.props.type.has(this.props.dates[date][i].kind)) {
                return true;
            }
        }
        return false;

    }

    render() {

        let dates = [];
        if (this.props.time == "past" || this.props.reverse) {
            let properties = Object.keys(this.props.dates).reverse();
            properties.forEach((date) => {
                if (this.props.dates[date].length !== 0 && this.dateContainType(date)) {
                    dates.push(<DateSection type={this.props.type} date={date} events={this.props.dates[date]} />);
                }
            });

        } else {
            for (const date in this.props.dates) {
                if (this.props.dates[date].length !== 0 && this.dateContainType(date)) {
                    dates.push(<DateSection type={this.props.type} date={date} events={this.props.dates[date]} />);
                }

            }
        }
        return <div className={"datebox"}>
            {dates}
        </div>;
    }
}

