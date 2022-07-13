lazy val root = (project in file(".")).
  settings(
    inThisBuild(List(
      organization := "com.example",
      scalaVersion := "3.1.3"
    )),
    name := "scalaleetcode"
  )

libraryDependencies += "org.scalatest" %% "scalatest" % "3.2.9" % Test
