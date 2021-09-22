library(shiny)

# Create static and dynamic tables
ui <- fluidPage(
    tableOutput("static"),
    dataTableOutput("dynamic")
)
server <- function(input, output, session) {
    output$static <- renderTable(head(mtcars))
    output$dynamic <- renderDataTable(mtcars, options = list(pageLength = 5))
}

# Run the application 
shinyApp(ui = ui, server = server)
