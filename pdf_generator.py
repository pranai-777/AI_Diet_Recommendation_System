from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(report, prediction, filename="diet_report.pdf"):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b>AI Diet Recommendation Report</b>",
            styles["Title"]
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            f"<b>Detected Food:</b> {prediction['food'].title()}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Confidence:</b> {prediction['confidence']*100:.2f}%",
            styles["Normal"]
        )
    )

    story.append(Spacer(1,15))

    story.append(
        Paragraph(
            "<b>Nutrition Facts</b>",
            styles["Heading2"]
        )
    )

    nutrition = report["nutrition"]

    for key, value in nutrition.items():

        story.append(
            Paragraph(
                f"{key}: {value}",
                styles["Normal"]
            )
        )

    story.append(Spacer(1,15))

    story.append(
        Paragraph(
            "<b>Diet Recommendation</b>",
            styles["Heading2"]
        )
    )

    recommendation = report["recommendation"]

    story.append(
        Paragraph(
            f"Best Time: {recommendation['best_time']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Benefit: {recommendation['benefit']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Water Intake: {recommendation['water']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Pair With: {recommendation['pair_with']}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1,15))

    story.append(
        Paragraph(
            "<b>Healthy Recipes</b>",
            styles["Heading2"]
        )
    )

    recipes = report["recipes"].head(5)

    for _, row in recipes.iterrows():

        story.append(
            Paragraph(
                f"• {row['name']} ({row['minutes']} min)",
                styles["Normal"]
            )
        )

    doc.build(story)

    return filename