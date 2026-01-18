'use strict';

const e = React.createElement;

class Itinerary extends React.Component {
    constructor(props) {
        super(props);
        this.state = { clicked: false, order: "split", reverse: false, type: new Set(), searchResults: {}, searching: false };
    }

    render() {
        const typeOptions = { "LS": "Lecture", "EX": "Exercise", "RD": "Reading", "PJ": "Project", "RV": "Review", "QZ": "Quiz", "WD": "Wellness", "FN": "Final" }
        const orderOptions = { "split": "Future/Past", "reverse": "Reverse", "chron": "In-Order" }
        const searching = this.state.searching

        const headRow = <div className="row headRow">
            <div className="col-6 itinerary-110-col">
                <h2 className="display-5 itinerary-heading">Comp110 Itinerary</h2>
            </div>
            <Search data={this.props.dates} defaultText={"Search..."} callback={(searching, results) => { this.setState({ searching: searching, searchResults: results }); console.log(this.state) }} />
            <div className="col">
                <button id="filter-button" className="btn" onClick={() => this.setState({ clicked: !this.state.clicked })}>
                    Filter<img className="filter-icon" src={`/static/components/Itinerary/arrow-${this.state.clicked ? "up" : "down"}.png`}></img></button>
            </div>
        </div>

        const buttonRow = this.state.clicked && <div className="itinerary-row kris-stupid-margin">
            <div className="row button-row">
                <div className="col-3 left-pill-buttons">
                    <PillButtons name={"Order"} options={orderOptions} startKey={this.state.order} singleSelect={true} callback={(newOrder) => { this.setState({ order: newOrder }) }} />
                </div>

                <div className="col-9 right-pill-buttons">
                    <PillButtons name={"Type"} options={typeOptions} startKeys={this.state.type} callback={(type) => {
                        let newState = this.state.type
                        if (this.state.type.has(type)) {
                            this.state.type.delete(type)
                        } else {
                            this.state.type.add(type)
                        }
                        this.setState({ type: newState })

                    }} />
                </div>
            </div>

            <div className="row dropdown-row">
                <div className="col text-center">
                    <Dropdown name={"Order"} options={orderOptions} button={false} startKey={this.state.order} singleSelect={true} callback={(newOrder) => { this.setState({ order: newOrder }) }} />
                </div>
                <div className="col text-center">
                    <Dropdown name={"Type"} options={typeOptions} button={false} startKeys={this.state.type} callback={(type) => {
                        let newState = this.state.type
                        if (this.state.type.has(type)) {
                            this.state.type.delete(type)
                        } else {
                            this.state.type.add(type)
                        }
                        this.setState({ type: newState })
                    }} />
                </div>
            </div>
        </div>

        if (this.state.order === "split" && !searching) {
            return <div>
                {headRow}
                {buttonRow}
                <Dates time="future" dates={this.props.future} type={this.state.type} />
                <div className="row">
                    <div className="col-10">
                        <h2 className="display-5 itinerary-heading">The Past</h2>
                    </div>
                </div>
                <Dates time="past" dates={this.props.past} type={this.state.type} />
            </div>

        } else {
            if (Object.keys(this.state.searchResults).length === 0) {
                return <div>
                    {headRow}
                    {buttonRow}
                    <div className="row py-2">
                        <p>No results found.</p>
                    </div>
                </div>
            }
            return <div>
                {headRow}
                {buttonRow}
                <div className="row py-2">
                    <Dates time="all" dates={searching ? this.state.searchResults : this.props.dates} reverse={this.state.order === "reverse"} type={this.state.type} />
                </div>
            </div>
        }
    }
}

const domContainer = document.querySelector('#filter');


Promise.all([
    fetch('/static/components/Itinerary/future.json?version=' + Date.now()),
    fetch('/static/components/Itinerary/past.json?version=' + Date.now()),
    fetch('/static/components/Itinerary/data.json?version=' + Date.now())
]).then(function (responses) {
    return Promise.all(responses.map(function (response) {
        return response.json();
    }));
}).then(function (data) {
    ReactDOM.render(e(Itinerary, { future: data[0], past: data[1], dates: data[2] }), domContainer);
}).catch(function (error) {
    // if there's an error, log it
    console.log(error);
});
