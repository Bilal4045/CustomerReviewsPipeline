import DashboardHeader from "./components/DashboardHeader";
import SummaryCards from "./components/SummaryCards";
import DailyReviewChart from "./components/DailyReviewChart";
import ScoreDistributionChart from "./components/ScoreDistributionChart";
import MonthlyReviewChart from "./components/MonthlyReviewChart";
import TopProducts from "./components/TopProducts";
import WorstProducts from "./components/WorstProducts";
import MostReviewedProducts from "./components/MostReviewedProducts";
import TopReviewers from "./components/TopReviewers";
import MostHelpfulReviews from "./components/MostHelpfulReviews";

function App() {
  return (
    <main className="min-h-screen bg-gray-100 p-8">
      <div className="mx-auto max-w-7xl">
        <DashboardHeader />
        <SummaryCards />
        <DailyReviewChart />
        <ScoreDistributionChart />
        <MonthlyReviewChart />
        <div className="mt-8 grid grid-cols-1 gap-6 lg:grid-cols-3">
           <TopProducts />
           <WorstProducts />
           <MostReviewedProducts />
            </div>

            <div className="mt-8 grid grid-cols-1 gap-6 lg:grid-cols-2">
            <TopReviewers />
            <MostHelpfulReviews />
            </div>
      </div>
    </main>
  );
}

export default App;