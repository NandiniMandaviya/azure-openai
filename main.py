from utils.parsing_utils import process_text_files
from utils.chunk_utils import chunk_data

url_filename_mapping = {
    # L&T Corporate
    "https://www.larsentoubro.com/corporate/about-lt-group/overview/":
        "Larsen_Toubro_Overview.txt",

    "https://www.larsentoubro.com/corporate/about-lt-group/technology-for-growth/":
        "Larsen_Toubro_Technology_for_growth.txt",

    "https://www.larsentoubro.com/corporate/about-lt-group/awards-recognition/":
        "Larsen_Toubro_Awards_Recognition.txt",

    "https://www.larsentoubro.com/corporate/about-lt-group/leadership/":
        "Larsen_Toubro_Leadership.txt",

    "https://www.larsentoubro.com/corporate/about-lt-group/facilities/":
        "Larsen_Toubro_Facilities.txt",

    "https://www.larsentoubro.com/corporate/about-lt-group/experience-centre-mumbai/":
        "Larsen_Toubro_Experience_Centre_Mumbai.txt",

    # L&T Sustainability
    "https://www.lntsustainability.com/overview/":
        "LNT_Sustainability_Overview.txt",

    "https://www.lntsustainability.com/climate-strategy/":
        "LNT_Climate_Strategy.txt",

    "https://www.lntsustainability.com/environment/":
        "LNT_Environment.txt",

    "https://www.lntsustainability.com/green-business/":
        "LNT_Green_Business.txt",

    # L&T Careers
    "https://www.larsentoubro.com/corporate/careers/learning-development/":
        "LNT_Careers_Learning_Development.txt",

    "https://www.larsentoubro.com/corporate/careers/diversity-equity-inclusion/":
        "LNT_Careers_Diversity_Equity_Inclusion.txt",

    "https://www.larsentoubro.com/corporate/careers/recruitment-caution/":
        "LNT_Careers_Recruitment_Caution.txt",

    "https://www.larsentoubro.com/corporate/careers/campus-recruitment/":
        "LNT_Careers_Campus_Recruitment.txt",

    "https://www.larsentoubro.com/corporate/careers/re-entry-career-re-entry-for-women/":
        "LNT_Careers_Re_entry_for_Women.txt",

    # L&T Annual Reports
            # Annual Reports
    "https://investors.larsentoubro.com/upload/AnnualRep/FY2026AnnualRepLNTIARFY2026.pdf":
            "LT_Annual_Review_2026.pdf",
    
    "https://annualreview.larsentoubro.com/download/L&T-Annual-Review-2024.pdf":
            "LT_Annual_Review_2024.pdf",
    
    "https://investors.larsentoubro.com/upload/AnnualRep/FY2024AnnualRepLnT%20IAR24.pdf":
            "LT_Annual_Review_2023-24.pdf",
    
    "https://wikirate-production-storage.fra1.cdn.digitaloceanspaces.com/files/13829458/34805698.pdf":
            "LT_Annual_Review_2021.pdf",
    
    "https://annualreview.larsentoubro.com/download/L&T-Annual-Review-2020.pdf":
            "LT_Annual_Review_2020.pdf",
}


if __name__ == "__main__":
    #process_text_files(url_filename_mapping)
    chunk_data(url_filename_mapping)