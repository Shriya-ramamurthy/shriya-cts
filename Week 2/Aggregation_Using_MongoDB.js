db.students.aggregate([
  {
    $match: {
      department: "Computer Science"
    }
  },
  {
    $group: {
      _id: "$department",
      averageMarks: { $avg: "$marks" },
      studentCount: { $sum: 1 }
    }
  }
]);