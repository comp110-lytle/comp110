class EventObject {
    kind: "LS" | "RD" | "EX" | "PJ" | "RV" | "QZ" | "WD" | "FN";
    n: 0;
    title: string;
    date: string;
    deadline: string;
    links: object;
}

interface DateSectionProps {
    date: string;
    events: Array<EventObject>;
    type: Set<"LS" | "RD" | "EX" | "PJ" | "RV" | "QZ" | "WD" | "FN">;

}

class DateSection extends React.Component<DateSectionProps> {
    constructor(props) {
        super(props);
    }

    parseDay(date: Date) {
        let day: number = date.getDay();
        switch (day) {
            case 0: return "Sun";
            case 1: return "Mon";
            case 2: return "Tue";
            case 3: return "Wed";
            case 4: return "Thu";
            case 5: return "Fri";
            case 6: return "Sat";
        }
    }

    parseMonth(date: Date) {
        let month: number = date.getMonth() + 1;
        switch (month) {
            case 1: return "Jan";
            case 2: return "Feb";
            case 3: return "Mar";
            case 4: return "Apr";
            case 5: return "May";
            case 6: return "Jun";
            case 7: return "Jul";
            case 8: return "Aug";
            case 9: return "Sep";
            case 10: return "Oct";
            case 11: return "Nov";
            case 12: return "Dec";
        }
    }

    parseDate(isoDate: string) {
        let date = new Date(isoDate);
        // for some reason need to increase day by 1
        date.setDate(date.getDate() + 1);
        return `${this.parseDay(date)}, ${this.parseMonth(date)} ${date.getDate()}`;
    }

    render() {
        let events = [];
        if (!this.props.type.size) {
            for (let i = 0; i < this.props.events.length; i++) {
                events.push(<EventSection event={this.props.events[i]} />);
            }
        } else {
            for (let i = 0; i < this.props.events.length; i++) {
                if (this.props.type.has(this.props.events[i].kind)) {
                    events.push(<EventSection event={this.props.events[i]} />);
                }
            }
        }

        return <div className="row itinerary-row py-2">
            <div className="date col-3">{this.parseDate(this.props.date)}</div>
            <div className="plans col-9">{events}</div>
        </div>;

    }
}